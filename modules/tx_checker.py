import asyncio
import random

from eth_typing import ChecksumAddress
from loguru import logger
from web3 import AsyncWeb3
from eth_account import Account as EthereumAccount
from tabulate import tabulate
from web3.middleware import async_geth_poa_middleware

from config import RPC

from utils.password_handler import get_private_keys


async def get_nonce(address: ChecksumAddress):
    web3 = AsyncWeb3(
        AsyncWeb3.AsyncHTTPProvider(random.choice(RPC["base"]["rpc"])),
        middlewares=[async_geth_poa_middleware],
    )

    nonce = await web3.eth.get_transaction_count(address)

    return nonce


async def check_tx():
    tasks = []

    logger.info("Start transaction checker")

    private_keys = get_private_keys()

    for _id, pk in enumerate(private_keys, start=1):
        account = EthereumAccount.from_key(pk)

        tasks.append(asyncio.create_task(get_nonce(account.address), name=account.address))

    await asyncio.gather(*tasks)

    table = [[k, i.get_name(), i.result()] for k, i in enumerate(tasks, start=1)]

    headers = ["#", "Address", "Nonce"]

    print(tabulate(table, headers, tablefmt="github"))
