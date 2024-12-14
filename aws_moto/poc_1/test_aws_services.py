# test_aws_services.py

import pytest
import pandas as pd
from io import BytesIO
from mock_clients import s3_client, glue_client, athena_client
from sqlalchemy_fixture import sqlalchemy_engine

def create_glue_table_from_dataframe(glue_client, s3_client, database_name, table_name, dataframe, bucket_name, key):
    # Create S3 bucket
    s3_client.create_bucket(Bucket=bucket_name)

    # Convert DataFrame to CSV and upload to S3
    csv_buffer = BytesIO()
    dataframe.to_csv(csv_buffer, index=False)
    s3_client.put_object(Bucket=bucket_name, Key=key, Body=csv_buffer.getvalue())

    # Create Glue database
    glue_client.create_database(DatabaseInput={'Name': database_name})

    # Define the table schema based on DataFrame columns
    columns = [
        {'Name': col, 'Type': 'string'} for col in dataframe.columns
    ]

    # Create Glue table
    glue_client.create_table(
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

def test_create_glue_table_and_query(s3_client, glue_client, athena_client, sqlalchemy_engine):
    # Create a sample DataFrame
    df = pd.DataFrame({
        'column1': ['data1', 'data2'],
        'column2': ['data3', 'data4']
    })

    # Define parameters
    database_name = 'test_database'
    table_name = 'test_table'
    bucket_name = 'test-bucket'
    key = 'test_data/test.csv'

    # Create Glue table from DataFrame
    create_glue_table_from_dataframe(glue_client, s3_client, database_name, table_name, df, bucket_name, key)

    # Verify that the table was created
    response = glue_client.get_table(DatabaseName=database_name, Name=table_name)
    assert response['Table']['Name'] == table_name
    assert response['Table']['StorageDescriptor']['Location'] == f's3://{bucket_name}/{key}'

    # Use SQLAlchemy engine to query the mocked database
    query = f"SELECT * FROM {table_name}"

    # Mock the Athena query response
    query_execution_id = '1234-5678-91011'

    athena_client.start_query_execution = lambda QueryString, QueryExecutionContext, ResultConfiguration: {
        'QueryExecutionId': query_execution_id
    }

    athena_client.get_query_execution = lambda QueryExecutionId: {
        'QueryExecution': {
            'Status': {
                'State': 'SUCCEEDED'
            }
        }
    }

    athena_client.get_query_results = lambda QueryExecutionId, MaxResults: {
        'ResultSet': {
            'Rows': [
                {'Data': [{'VarCharValue': 'data1'}, {'VarCharValue': 'data3'}]},
                {'Data': [{'VarCharValue': 'data2'}, {'VarCharValue': 'data4'}]}
            ]
        }
    }

    # Execute the query using SQLAlchemy engine
    with sqlalchemy_engine.connect() as conn:
        result = conn.execute(query)
        rows = result.fetchall()
        assert rows == [('data1', 'data3'), ('data2', 'data4')]

# Additional tests can be added here
