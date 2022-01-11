import json
from importlib import resources

from ftmscan.core.async_client import AsyncClient
from ftmscan.core.base import BaseClient
from ftmscan.core.sync_client import SyncClient


class ftmScan:
    """Client factory."""

    def __new__(cls, api_key: str, asynchronous=True, debug=False) -> BaseClient:
        """Create a new client.
        Args:
            api_key (str): Your ftmscan.com API key.
            asynchronous (bool, optional): Whether client is async or not. Defaults to True.
            debug (bool, optional): Display generated URLs for debugging. Defaults to False.
        Returns:
            BaseClient: ftmscan client.
        """
        if asynchronous:
            return AsyncClient(api_key=api_key, debug=debug)
        return SyncClient(api_key=api_key, debug=debug)