import logging
import azure.functions as func
import pyodbc
import os
import json

def main(metadata: dict) -> None:
    logging.info(f"Storing metadata to database: {metadata}")

    server = os.getenv("SQL_SERVER")          # e.g., maryam-sqlserver.database.windows.net
    database = os.getenv("SQL_DATABASE")      # e.g., image-metadata-db
    username = os.getenv("SQL_USER")          # e.g., maryamadmin
    password = os.getenv("SQL_PASSWORD")      # e.g., your admin password
    driver = "{ODBC Driver 17 for SQL Server}"

    try:
        conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO metadata (fileName, fileSizeKB, width, height, format)
                VALUES (?, ?, ?, ?, ?)
                """,
                metadata["fileName"],
                metadata["fileSizeKB"],
                metadata["width"],
                metadata["height"],
                metadata["format"]
            )
            conn.commit()
        logging.info("✅ Metadata stored successfully.")
    except Exception as e:
        logging.error(f"❌ Error storing metadata: {e}")
