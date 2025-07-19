import azure.functions as func
import logging
import asyncio
from azure.durable_functions import DurableOrchestrationClient

async def main(blob: func.InputStream, starter: str):
    logging.info(f"Blob trigger function processed blob: {blob.name}")

    # Extract only the blob name without the container prefix
    blob_name = blob.name.split("/")[-1]

    client = DurableOrchestrationClient(starter)

    instance_id = await client.start_new("OrchestratorFunction", None, blob_name)

    logging.info(f"Started orchestration with ID = '{instance_id}' for blob '{blob_name}'")
