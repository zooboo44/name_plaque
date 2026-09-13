import os
from pathlib import Path
from dotenv import load_dotenv
from azure.identity import (DeviceCodeCredential, TokenCachePersistenceOptions, AuthenticationRecord)
from msgraph import GraphServiceClient

class Graph:

    def __init__(self, env_file=".env"):
        load_dotenv(env_file)

        client_id = os.getenv("CLIENT_ID")
        tenant_id = os.getenv("TENANT_ID")
        self.graph_scope = os.getenv("SCOPE").split()

        self.auth_record_file = Path(".auth_record")

        cache_options = TokenCachePersistenceOptions(name="myapp", allow_unencrypted_storage=True)

        authentication_record = None

        if self.auth_record_file.exists():
            with open(self.auth_record_file, "rb") as f:
                params = f.read().decode("utf-8")
                authentication_record = AuthenticationRecord.deserialize(params)

        self.device_code_credential = DeviceCodeCredential(
            client_id,
            tenant_id=tenant_id,
            cache_persistence_options=cache_options,
            authentication_record=authentication_record
        )

        self.user_client = GraphServiceClient(
            self.device_code_credential,
            self.graph_scope
        )

    def authenticate(self):
        record = self.device_code_credential.authenticate(scopes=self.graph_scope)

        with open(self.auth_record_file, "wb") as f:
            f.write(record.serialize().encode("utf-8"))

    async def get_presence(self):
        presence = await self.user_client.me.presence.get()
        return presence.availability