import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):
    blob_name = context.get_input()

    metadata = yield context.call_activity("ExtractMetadataActivity", blob_name)
    result = yield context.call_activity("StoreMetadataActivity", metadata)

    return {"status": "Done", "metadata": metadata, "db_response": result}

main = df.Orchestrator.create(orchestrator_function)
