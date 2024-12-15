# mock_clients.py

import pytest
import boto3
from moto import mock_aws


@pytest.fixture(scope="session")
def s3_client():
    with mock_aws():
        s3 = boto3.client("s3")
        yield s3


@pytest.fixture(scope="session")
def glue_client():
    with mock_aws():
        glue = boto3.client("glue")
        yield glue


@pytest.fixture(scope="session")
def athena_client():
    with mock_aws():
        athena = boto3.client("athena")
        yield athena
