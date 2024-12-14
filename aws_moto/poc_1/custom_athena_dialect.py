# custom_athena_dialect.py

from sqlalchemy.engine import create_engine


def mock_create_engine(database_name, s3_staging_dir):
    # Create a mocked Athena engine
    return create_engine(
        f"awsathena+rest://@athena.us-east-1.amazonaws.com:443/"
        f"{database_name}?s3_staging_dir={s3_staging_dir}"
    )
