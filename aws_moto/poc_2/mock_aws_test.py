# Usage in a test file
import pytest
from mock_aws_service import MockAWSService
import pandas as pd

@pytest.fixture(scope='module')
def mock_aws_service():
    service = MockAWSService()
    service.setup()
    yield service
    service.teardown()

def test_create_glue_table_and_query(mock_aws_service):
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
    mock_aws_service.create_glue_table_from_dataframe(database_name, table_name, df, bucket_name, key)

    # Verify that the table was created
    response = mock_aws_service.glue_client.get_table(DatabaseName=database_name, Name=table_name)
    assert response['Table']['Name'] == table_name
    assert response['Table']['StorageDescriptor']['Location'] == f's3://{bucket_name}/{key}'

    # Execute the query using pd.read_sql_query
    query = f"SELECT * FROM {table_name}"
    df_result = mock_aws_service.execute_query(query)

    # Convert DataFrame result to list of tuples for assertion
    rows = [tuple(row) for row in df_result.to_numpy()]
    assert rows == [('data1', 'data3'), ('data2', 'data4')]