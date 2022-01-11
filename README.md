# ftmscan-python

<p align="center">
  <a href="https://github.com/tarsil/ftmscan-python" alt="build">
        <img src="https://github.com/tarsil/ftmscan-python/workflows/build/badge.svg" /></a>
</p>

<p align="center">
  <a href="https://badge.fury.io/py/ftmscan-python" alt="pypi">
        <img src="https://badge.fury.io/py/ftmscan-python.svg" /></a>
  
  <a href="" alt="license">
        <img src="https://img.shields.io/github/license/awilliamson10/ftmscan-python" /></a>
  
  <a href="https://www.python.org/downloads/release/python-385/" alt="python-version">
        <img src="https://img.shields.io/badge/python-3.8-blue.svg" /></a>
</p>

<p align="center">
  A complete Python API for <a href="https://ftmscan.com/">FTMscan.com</a>
</p>

<p align="center">
  Powered by <a href="https://ftmscan.com/apis">FTMscan.com APIs</a>
</p>

<p align="center">
  Available on <a href="https://pypi.org/project/ftmscan-python/">PyPI</a> 
</p>


<p align="center">
  <i>A fork of the <a href="https://github.com/tarsil/polygonscan-python">polygonscan-python</a> package.</i>
</p>

A minimal, yet complete, Python API for [ftmscan.com](https://ftmscan.com/).

This package was cloned from [polygonscan-python](https://github.com/tarsil/polygonscan-python) and readapted to ftm network. A special thanks to the [creator](https://github.com/tarsil).
Without his hardwork this would be possible.

Available on [PyPI](https://pypi.org/project/ftmscan-python/). Powered by [ftmscan.com APIs](https://ftmscan.com/apis#misc).

___

## Endpoints

The following endpoints are provided:

<details><summary>Accounts <a href="https://ftmscan.com/apis#accounts">(source)</a></summary>
<p>

* `get_ftm_balance`
* `get_ftm_balance_multiple`
* `get_normal_txs_by_address`
* `get_normal_txs_by_address_paginated`
* `get_internal_txs_by_address`
* `get_internal_txs_by_address_paginated`
* `get_internal_txs_by_txhash`
* `get_internal_txs_by_block_range_paginated`
* `get_erc20_token_transfer_events_by_address`
* `get_erc20_token_transfer_events_by_contract_address_paginated`
* `get_erc20_token_transfer_events_by_address_and_contract_paginated`
* `get_erc721_token_transfer_events_by_address`
* `get_erc721_token_transfer_events_by_contract_address_paginated`
* `get_erc721_token_transfer_events_by_address_and_contract_paginated`
* `get_mined_blocks_by_address`
* `get_mined_blocks_by_address_paginated`

</details>

<details><summary>Contracts <a href="https://ftmscan.com/apis#contracts">(source)</a></summary>
<p>
  
* `get_contract_abi`
* `get_contract_source_code`

</details>

</details>

<details><summary>Tokens <a href="https://ftmscan.com/apis#tokens">(source)</a></summary>
<p>
  
* `get_total_supply_by_contract_address`
* `get_acc_balance_by_token_and_contract_address`

</details>

<details><summary>Stats <a href="https://ftmscan.com/apis#stats">(source)</a></summary>
<p>
  
* `get_total_ftm_supply`
* `get_ftm_last_price`

</details>

*If you think that a newly-added method is missing, kindly open an [issue](https://github.com/awilliamson10/ftmscan-python/issues) as a feature request and I will do my best to add it.*

## Installation

Before proceeding, you should register an account on [ftmscan.com](https://ftmscan.com/)
and [generate a personal API key](https://ftmscan.com/myapikey) to use.

If you wish to have access to the PRO endpoints, you should obtain elevated privileges via ftmScans's
subscription service.

Install from source:

``` bash
pip install git+https://github.com/awilliamson10/ftmscan-python
```

Alternatively, install from [PyPI](https://pypi.org/project/ftmscan-python/):

```bash
pip install ftmscan-python
```

## Unit tests

In `bash`, test that everything looks OK on your end using your `YOUR_API_KEY` (without quotation marks)
before proceeding:

``` bash
bash run_tests.sh YOUR_API_KEY
````

This will regenerate the logs under `logs/` with the most recent results and the timestamp of the execution.

## Usage

In `python`, create a client with your personal [ftmscan.com](https://ftmscan.com/) API key:

E.g:
``` python
from ftmscan import ftmScan

with ftmScan("API_KEY",False) as ftm:
    print(ftm.get_ftm_balance(address="0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a"))
```

Then you can call all available methods, e.g.:

``` python
ftm.get_ftm_balance(address="0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a")

> '40891631566070000000000'
```

## Examples

Examples (arguments and results) for all methods may be found as JSON files
[here](https://github.com/tarsil/ftmscan-python/tree/master/logs).
For example, if you want to use the method `get_block_number_by_timestamp`,
you can find the supported arguments and the format of its output in its respective 
[JSON file](logs/standard/get_block_number_by_timestamp.json):

``` json
{
  "method": "get_block_number_by_timestamp",
  "module": "blocks",
  "kwargs": {
    "timestamp": "1578638524",
    "closest": "before"
  },
  "log_timestamp": "2020-10-28-12:34:44",
  "res": "9251482"
}
```

where `kwargs` refer to the required named arguments and `res` refers to the expected result if you were to run:

``` python
eth.get_block_number_by_timestamp(timestamp="1578638524", closest="before")

> '9251482'
```

**Disclaimer**: Those examples blindly use the arguments originally showcased
[here](https://api.ftmscan.com/apis) and the selected wallets/contracts
do not reflect any personal preference. You should refer to the same source for additional
information regarding specific argument values.

## Issues

For problems regarding installing or using the package please open an
[issue](https://github.com/tarsil/ftmscan-python/issues).
Kindly avoid disclosing potentially sensitive information such as your API keys or your wallet addresses.

Feel free to leave a :star: if you found this package useful.

___

 Powered by [ftmscan.com APIs](https://ftmscan.com/apis).
