import awswrangler as wr


def hive_table_exists(conn, database: str, table: str) -> bool:
    """Check if table exists in Hive."""
    return wr.catalog.does_table_exist(database=database, table=table)
