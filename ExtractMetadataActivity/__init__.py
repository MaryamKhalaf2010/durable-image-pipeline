import os
from PIL import Image
from io import BytesIO
from azure.storage.blob import BlobServiceClient
import logging

def main(blob_name: str) -> dict:
    try:
        connection_string = os.environ["BlobStorageConnectionString"]
        container_name = "images-input"

        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_container_client(container_name).get_blob_client(blob_name)
        blob_data = blob_client.download_blob().readall()

        image = Image.open(BytesIO(blob_data))

        metadata = {
            "fileName": blob_name,
            "fileSizeKB": round(len(blob_data) / 1024, 2),
            "width": image.width,
            "height": image.height,
            "format": image.format
        }

        logging.info(f"Extracted metadata: {metadata}")
        return metadata

    except Exception as e:
        logging.error(f"Metadata extraction failed: {e}")
        raise
