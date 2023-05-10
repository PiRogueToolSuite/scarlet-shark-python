from scarlet_shark_client.clients.v04_client import ScarletSharkClient as V04ScarletSharkClient
from scarlet_shark_client.clients.abstract import ScarletSharkClient

API_CLIENTS = {
    'v0.4': V04ScarletSharkClient,
}


class ClientFactory:
    @staticmethod
    def get_client(api_key: str, api_version: str = 'v0.4', print_json=False) -> ScarletSharkClient:
        if api_version not in API_CLIENTS:
            raise Exception(f'No Scarlet Shark client is available for the given version {api_version}')
        return API_CLIENTS[api_version](api_key, print_json)

    @staticmethod
    def get_supported_versions():
        return list(API_CLIENTS.keys())
