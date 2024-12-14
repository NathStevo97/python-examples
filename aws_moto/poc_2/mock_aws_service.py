import boto3
from moto import mock_aws
from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
import pandas as pd
from io import BytesIO
import logging

class MockAWSService:
    def __init__(self):
        self.s3_client = None
        self.glue_client = None
        self.athena_client = None
        self.engine = None
        logging.basicConfig(level=logging.DEBUG)

    def setup(self):
        self.mock = mock_aws()
        self.mock.start()

        self.s3_client = boto3.client('s3', region_name='us-east-1')
        self.glue_client = boto3.client('glue', region_name='us-east-1')
        self.athena_client = boto3.client('athena', region_name='us-east-1')

        # Use in-memory SQLite for testing instead of Athena
        self.engine = create_engine(
            'sqlite:///:memory:',
            connect_args={'check_same_thread': False},
            poolclass=StaticPool
        )

    def teardown(self):
        self.mock.stop()

    def create_glue_table_from_dataframe(self, database_name, table_name, dataframe, bucket_name, key):
        # Create S3 bucket
        self.s3_client.create_bucket(Bucket=bucket_name)

        # Convert DataFrame to CSV and upload to S3
        csv_buffer = BytesIO()
        dataframe.to_csv(csv_buffer, index=False)
        self.s3_client.put_object(Bucket=bucket_name, Key=key, Body=csv_buffer.getvalue())

        # Create Glue database
        self.glue_client.create_database(DatabaseInput={'Name': database_name})

        # Define the table schema based on DataFrame columns
        columns = [
            {'Name': col, 'Type': 'string'} for col in dataframe.columns
        ]

        # Create Glue table
        self.glue_client.create_table(
            DatabaseName=database_name,
            TableInput={
                'Name': table_name,
                'StorageDescriptor': {
                    'Columns': columns,
                    'Location': f's3://{bucket_name}/{key}',
                    'InputFormat': 'org.apache.hadoop.mapred.TextInputFormat',
                    'OutputFormat': 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
                    'SerdeInfo': {
                        'SerializationLibrary': 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe',
                        'Parameters': {
                            'field.delim': ','
                        }
                    }
                }
            }
        )

        # Create table in in-memory SQLite database
        dataframe.to_sql(table_name, self.engine, index=False, if_exists='replace')

    def execute_query(self, query):
        logging.debug(f"Executing query: {query}")
        with self.engine.connect() as conn:
            df_result = pd.read_sql_query(text(query), conn)
        logging.debug(f"Query result: {df_result}")
        return df_result