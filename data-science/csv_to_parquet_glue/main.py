import pandas as pd
import awswrangler as wr
import boto3


def convert_csv_to_parquet_and_create_glue_table(
    csv_path, s3_bucket, s3_key, glue_database, glue_table_name
):
    # Step 1: Read the CSV file using pandas
    print("Reading CSV file...")
    df = pd.read_csv(csv_path)

    # Step 2: Save the DataFrame as a Parquet file
    print("Converting to Parquet and uploading to S3...")
    wr.s3.to_parquet(
        df=df,
        path=f"s3://{s3_bucket}/{s3_key}",
        dataset=True,
        database=glue_database,
        table=glue_table_name,
        mode="overwrite",
    )

    print("Process complete. AWS Glue table created.")


# Example usage
if __name__ == "__main__":
    # Configuration
    csv_file_path = "Housing.csv"  # Local CSV file path
    s3_bucket_name = "demo-database-s3-bucket"
    s3_object_key = "your/parquet/output/"  # Ensure it ends with a slash for datasets
    glue_db_name = "demo-database"
    glue_table = "your_glue_table"

    convert_csv_to_parquet_and_create_glue_table(
        csv_path=csv_file_path,
        s3_bucket=s3_bucket_name,
        s3_key=s3_object_key,
        glue_database=glue_db_name,
        glue_table_name=glue_table,
    )
