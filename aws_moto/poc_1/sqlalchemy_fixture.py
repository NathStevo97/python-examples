# sqlalchemy_fixture.py

import pytest
from custom_athena_dialect import mock_create_engine

@pytest.fixture(scope="session")
def sqlalchemy_engine(athena_client):
    # Mock the SQLAlchemy engine to use the mocked Athena
    database_name = 'test_database'
    s3_staging_dir = 's3://mocked-staging-dir/'
    engine = mock_create_engine(database_name, s3_staging_dir)
    yield engine

