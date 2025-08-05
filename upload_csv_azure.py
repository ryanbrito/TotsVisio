from azure.storage.blob import BlobServiceClient
import os

# Configurações
AZURE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=totsvisiodb;AccountKey=XT1NpUL9UrN+2bTCRV6qEqcts0Psweg8o96hrlsnxgNR2CeOhIkPFU2yU/0CtxABmTTLqJkHN3zg+AStVIGOeg==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "csvs-tratados-gpt"
LOCAL_DIR = r"C:\Users\guilherme.barbosa\OneDrive - engeform\Área de Trabalho\projeto_tratamento_csv\dados_tratados"

# Conectar ao serviço
blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

# Upload de todos os CSVs da pasta
for file_name in os.listdir(LOCAL_DIR):
    if file_name.endswith(".csv"):
        blob_client = container_client.get_blob_client(file_name)
        file_path = os.path.join(LOCAL_DIR, file_name)
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        print(f"✔ Arquivo '{file_name}' enviado com sucesso.")
