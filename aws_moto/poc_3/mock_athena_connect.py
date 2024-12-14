import boto3
from moto import mock_aws
from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
import pandas as pd
from io import BytesIO
import logging

class MockAthenaConnect:
    def __init__(self):
        self.s3_client = None
        self.glue_client = None
        self.athena_client = None
        self.engine = None
        self.bucket_name = 'test-bucket'
        self.database_name = 'test_database'
        logging.basicConfig(level=logging.DEBUG)
        self.setup()

    def setup(self):
        self.mock = mock_aws()
        self.mock.start()

        self.s3_client = boto3.client('s3', region_name='eu-west-2')
        self.glue_client = boto3.client('glue', region_name='eu-west-2')
        self.athena_client = boto3.client('athena', region_name='eu-west-2')

        # Set up SQLAlchemy engine to connect to Athena
        self.engine = create_engine(
            'awsathena+rest://@athena.eu-west-2.amazonaws.com:443/',
            connect_args={
                's3_staging_dir': 's3://test-bucket/your-athena-query-results/',
                'region_name': 'eu-west-2'
            }
        )

        # Set up in-memory SQLite database to simulate Athena
        #self.engine = create_engine('sqlite:///:memory:', echo=True)

        # Create S3 bucket
        try:
            self.s3_client.create_bucket(
                Bucket=self.bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': 'eu-west-2'
                })
        except self.s3_client.exceptions.BucketAlreadyOwnedByYou:
            logging.debug("Bucket already exists and is owned by you")

        # Create Glue database
        try:
            self.glue_client.create_database(DatabaseInput={'Name': self.database_name})
        except self.glue_client.exceptions.AlreadyExistsException:
            logging.debug("Glue database already exists")

    def teardown(self):
        # Empty and delete the S3 bucket
        s3_resource = boto3.resource('s3', region_name='eu-west-2')
        bucket = s3_resource.Bucket(self.bucket_name)
        bucket.objects.all().delete()
        self.s3_client.delete_bucket(Bucket=self.bucket_name)

        # Delete Glue database
        try:
            self.glue_client.delete_database(Name=self.database_name)
        except self.glue_client.exceptions.EntityNotFoundException:
            logging.debug("Glue database not found")

        self.mock.stop()

    def create_glue_table_from_dataframe(self, table_name, dataframe, key):
        # Convert DataFrame to CSV and upload to S3
        csv_buffer = BytesIO()
        dataframe.to_csv(csv_buffer, index=False)
        self.s3_client.put_object(Bucket=self.bucket_name, Key=key, Body=csv_buffer.getvalue())

        # Define the table schema based on DataFrame columns
        columns = [{'Name': col, 'Type': 'string'} for col in dataframe.columns]

        # Check if the table already exists and delete it if it does
        try:
            self.glue_client.get_table(DatabaseName=self.database_name, Name=table_name)
            self.glue_client.delete_table(DatabaseName=self.database_name, Name=table_name)
            logging.debug(f"Deleted existing Glue table: {table_name}")
        except self.glue_client.exceptions.EntityNotFoundException:
            logging.debug(f"Glue table {table_name} does not exist")

        # Create Glue table
        self.glue_client.create_table(
            DatabaseName=self.database_name,
            TableInput={
                'Name': table_name,
                'StorageDescriptor': {
                    'Columns': columns,
                    'Location': f's3://{self.bucket_name}/{key}',
                    'InputFormat': 'org.apache.hadoop.mapred.TextInputFormat',
                    'OutputFormat': 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
                    'SerdeInfo': {
                        'SerializationLibrary': 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe',
                        'Parameters': {'field.delim': ','}
                    }
                }
            }
        )

        # Create the table in SQLite for querying
        #dataframe.to_sql(table_name, self.engine, index=False, if_exists='replace')

    def execute_query(self, query):
        logging.debug(f"Executing query: {query}")
        with self.engine.connect() as conn:
            df_result = pd.read_sql_query(text(query), conn)
        logging.debug(f"Query result: {df_result}")
        return df_result

    def mock_athena_response(self, query, results):
        # Execute a query in the mocked Athena environment
        response = self.athena_client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={'Database': self.database_name},
            ResultConfiguration={'OutputLocation': f's3://{self.bucket_name}/results/'}
        )
        query_execution_id = response['QueryExecutionId']

        # Wait for query execution to complete
        self.athena_client.get_query_execution = lambda QueryExecutionId: {
            'QueryExecution': {
                'Status': {'State': 'SUCCEEDED'}
            }
        }

        # Mock the query results
        self.athena_client.get_query_results = lambda QueryExecutionId, MaxResults: {
            'ResultSet': {
                'Rows': [{'Data': [{'VarCharValue': value} for value in row]} for row in results]
            }
        }
        return query_execution_id
