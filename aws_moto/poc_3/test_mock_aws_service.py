import pytest
import pandas as pd
from aws_moto.poc_3.mock_athena_connect import MockAandiConnect
from aws_moto.poc_3.utility_functions import hive_table_exists
from unittest.mock import patch

@pytest.fixture(scope='session')
def mock_aandi_connect():
    service = MockAandiConnect()
    yield service
    service.teardown()

def test_hive_table_exists(mock_aandi_connect):
    # Create a sample DataFrame
    df = pd.DataFrame({
        'column1': ['data1', 'data2'],
        'column2': ['data3', 'data4']
    })

    # Define parameters
    table_name = 'test_table'
    key = 'test_data/test.csv'

    # Create Glue table from DataFrame
    mock_aandi_connect.create_glue_table_from_dataframe(table_name, df, key)

    # Verify that the table exists using hive_table_exists
    with mock_aandi_connect.engine.connect() as conn:
        table_exists = hive_table_exists(conn, mock_aandi_connect.database_name, table_name)
    assert table_exists
    # Create a sample DataFrame
    df = pd.DataFrame({
        'column1': ['data1', 'data2'],
        'column2': ['data3', 'data4']
    })

    # Define parameters
    table_name = 'test_table'
    key = 'test_data/test.csv'

    # Create Glue table from DataFrame
    mock_aandi_connect.create_glue_table_from_dataframe(table_name, df, key)

    # Verify that the table was created
    response = mock_aandi_connect.glue_client.get_table(DatabaseName=mock_aandi_connect.database_name, Name=table_name)
    assert response['Table']['Name'] == table_name
    assert response['Table']['StorageDescriptor']['Location'] == f's3://{mock_aandi_connect.bucket_name}/{key}'
    with mock_aandi_connect.engine.connect() as conn:
        assert hive_table_exists(conn, mock_aandi_connect.database_name, table_name)

def test_create_new_table_from_query(mock_aandi_connect):
    # Create a sample DataFrame for static_test_labels
    df = pd.DataFrame({
        'column1': ['data1', 'data2'],
        'column2': ['data3', 'data4']
    })

    # Define parameters
    original_table_name = 'static_test_labels'
    new_table_name = 'test_labels'
    key = 'test_data/static_test_labels.csv'

    # Create Glue table from DataFrame
    mock_aandi_connect.create_glue_table_from_dataframe(original_table_name, df, key)

    # Verify that the original table was created
    response = mock_aandi_connect.glue_client.get_table(DatabaseName=mock_aandi_connect.database_name, Name=original_table_name)
    assert response['Table']['Name'] == original_table_name
    assert response['Table']['StorageDescriptor']['Location'] == f's3://{mock_aandi_connect.bucket_name}/{key}'

    # Mock the Athena responses for the new table creation
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {mock_aandi_connect.database_name}.{new_table_name} AS
    SELECT * FROM {mock_aandi_connect.database_name}.{original_table_name}
    """

    # Execute the create table query using wr.athena.read_sql_query
    df_result = mock_aandi_connect.execute_query(create_table_query)

    # Verify that the new table was created
    response = mock_aandi_connect.glue_client.get_table(DatabaseName=mock_aandi_connect.database_name, Name=new_table_name)
    assert response['Table']['Name'] == new_table_name

    # Optionally, verify that the table exists using hive_table_exists function
    with mock_aandi_connect.engine.connect() as conn:
        table_exists = hive_table_exists(conn, mock_aandi_connect.database_name, new_table_name)
    assert table_exists

    # List all tables in the database for debugging
    tables = mock_aandi_connect.glue_client.get_tables(DatabaseName=mock_aandi_connect.database_name)
    print("Tables in database:", [table['Name'] for table in tables['TableList']])