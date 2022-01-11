import asyncio
import json
import os
from datetime import datetime
from unittest import IsolatedAsyncioTestCase

from ftmscan import ftmScan

CONFIG_PATH = "ftmscan/configs/stable.json"
API_KEY = os.environ["API_KEY"]


def load(fname):
    with open(fname, "r") as f:
        return json.load(f)


def dump(data, fname):
    with open(fname, "w") as f:
        json.dump(data, f, indent=2)


class Case(IsolatedAsyncioTestCase):
    _MODULE = ""

    async def test_methods(self):
        print(f"\nMODULE: {self._MODULE}")
        config = load(CONFIG_PATH)
        async with ftmScan(api_key=API_KEY, asynchronous=True, debug=True) as ftm:
            for fun, v in config.items():
                if not fun.startswith("_"):  # disabled if _
                    if v["module"] == self._MODULE:
                        res = await getattr(ftm, fun)(**v["kwargs"])
                        print(f"ASYNC: True, METHOD: {fun}, RTYPE: {type(res)}")
                        fname = f"logs/standard/{fun}.json"
                        log = {
                            "method": fun,
                            "module": v["module"],
                            "kwargs": v["kwargs"],
                            "log_timestamp": datetime.now().strftime(
                                "%Y-%m-%d-%H:%M:%S"
                            ),
                            "res": res,
                        }
                        dump(log, fname)
                        await asyncio.sleep(0.5)


class TestAccounts(Case):
    _MODULE = "accounts"


class TestBlocks(Case):
    _MODULE = "blocks"


class TestContracts(Case):
    _MODULE = "contracts"


class TestLogs(Case):
    _MODULE = "logs"


class TestProxy(Case):
    _MODULE = "proxy"


class TestStats(Case):
    _MODULE = "stats"


class TestTokens(Case):
    _MODULE = "tokens"


class TestTransactions(Case):
    _MODULE = "transactions"