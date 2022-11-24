# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging

import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

#connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
#print(connect_str)
def main(containerinput: str) -> list:
    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=ass2durablefn;AccountKey=lJJB91Rhmht7G77pBrByznAOWKw9P9yX/wFDZEKePz/FD+AaxigokNfvl+ZlEIAe9A8GWo18+Brl+AStwap41Q==;EndpointSuffix=core.windows.net")
    #blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(container=containerinput)
    blobs = container_client.list_blobs()
    res = []
    for blob in blobs:
        input_text = container_client.download_blob(blob.name).readall()
        print(input_text)
        split_lines = input_text.splitlines() 
        lines_list = []
        line_num = 0
        for each in split_lines:
            line_num = line_num + 1
            lines_list.append((line_num, str(each)))
        res.extend(lines_list)
    return res
