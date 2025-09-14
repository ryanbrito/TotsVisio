from azure.storage.blob import BlobServiceClient

# Configurações
AZURE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=totsvisiodb;AccountKey=XT1NpUL9UrN+2bTCRV6qEqcts0Psweg8o96hrlsnxgNR2CeOhIkPFU2yU/0CtxABmTTLqJkHN3zg+AStVIGOeg==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "csvs-tratados-gpt"

# Conectar ao serviço
blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

# Listar arquivos
print("📂 Listando arquivos presentes no container:")
blobs = list(container_client.list_blobs())

if blobs:
    for blob in blobs:
        print(f" - {blob.name}")
else:
    print("⚠ Nenhum arquivo encontrado no container.")
