import os
from dotenv import load_dotenv
from azure.identity import DeviceCodeCredential
from msgraph import GraphServiceClient

class Graph:

    def __init__(self, env_file=".env"):
        load_dotenv(env_file)
        client_id = os.getenv("CLIENT_ID")
        tenant_id = os.getenv("TENANT_ID")
        graph_scope = os.getenv("SCOPE").split()

        self.hello_world = "Hello world"
        self.device_code_credential = DeviceCodeCredential(client_id, tenant_id=tenant_id)
        self.user_client = GraphServiceClient(self.device_code_credential, graph_scope)

    async def print_presence(self):
        presence = await self.user_client.me.presence.get()
        print(presence.availability)
        print(presence.activity)