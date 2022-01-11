import os
from unittest import TestCase
from unittest.async_case import IsolatedAsyncioTestCase

from aiohttp import ClientSession
from ftmscan.core.async_client import AsyncClient
from ftmscan.core.sync_client import SyncClient

from requests import Session

CONFIG_PATH = "ftm/configs/stable.json"
API_KEY = os.environ["API_KEY"]


class TestSyncSession(TestCase):
    def test_from_session_sync(self):
        client = SyncClient.from_session(
            api_key=API_KEY,
            session=Session(),
        )
        self.assertTrue(client.get_ftm_last_price())


class TestAsyncSession(IsolatedAsyncioTestCase):
    async def test_from_session_async(self):
        client = await AsyncClient.from_session(
            api_key=API_KEY,
            session=ClientSession(),
        )
        self.assertTrue(await client.get_ftm_last_price())