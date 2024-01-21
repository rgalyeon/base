import asyncio
import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import questionary
from questionary import Choice

from settings import (
    RANDOM_WALLET,
    SLEEP_TO,
    SLEEP_FROM,
    QUANTITY_THREADS,
    THREAD_SLEEP_FROM,
    THREAD_SLEEP_TO, REMOVE_WALLET,
)
from modules_settings import *
from utils.helpers import remove_wallet
from utils.sleeping import sleep
from utils.password_handler import get_private_keys
from utils.logs_handler import filter_out_utils
from itertools import count


from loguru import logger


def get_module():
    counter = count(1)
    result = questionary.select(
        "Select a method to get started",
        choices=[
            Choice(f"{next(counter)}) Encrypt wallets", encrypt_privates),
            Choice(f"{next(counter)}) Withdraw from OKX", withdraw_okx),
            Choice(f"{next(counter)}) Make bridge to Base", bridge_base),
            Choice(f"{next(counter)}) Make bridge on Orbiter", bridge_orbiter),
            Choice(f"{next(counter)}) Wrap ETH", wrap_eth),
            Choice(f"{next(counter)}) Unwrap ETH", unwrap_eth),
            Choice(f"{next(counter)}) Swap on Uniswap", swap_uniswap),
            Choice(f"{next(counter)}) Swap on Pancake", swap_pancake),
            Choice(f"{next(counter)}) Swap on WooFi", swap_woofi),
            Choice(f"{next(counter)}) Swap on BaseSwap", swap_baseswap),
            Choice(f"{next(counter)}) Swap on AlienSwap", swap_alienswap),
            Choice(f"{next(counter)}) Swap on Maverick", swap_maverick),
            Choice(f"{next(counter)}) Swap on Odos", swap_odos),
            Choice(f"{next(counter)}) Swap on 1inch", swap_inch),
            Choice(f"{next(counter)}) Swap on OpenOcean", swap_openocean),
            Choice(f"{next(counter)}) Swap on XYSwap", swap_xyswap),
            Choice(f"{next(counter)}) Bungee Refuel", bungee_refuel),
            Choice(f"{next(counter)}) Stargate bridge", stargate_bridge),
            Choice(f"{next(counter)}) Deposit Aave", deposit_aave),
            Choice(f"{next(counter)}) Withdraw Aave", withdraw_aave),
            Choice(f"{next(counter)}) Deposit MoonWell", deposit_moonwell),
            Choice(f"{next(counter)}) Withdraw MoonWell", withdraw_moonwell),
            Choice(f"{next(counter)}) Mint NFT on MintFun", mint_mintfun),
            Choice(f"{next(counter)}) Mint and Bridge Zerius NFT", mint_zerius),
            Choice(f"{next(counter)}) Mint ZkStars NFT", mint_zkstars),
            Choice(f"{next(counter)}) Dmail sending mail", send_mail),
            Choice(f"{next(counter)}) Send message L2Telegraph", send_message),
            Choice(f"{next(counter)}) Mint and bridge NFT L2Telegraph", bridge_nft),
            Choice(f"{next(counter)}) Create portfolio on Ray", create_portfolio),
            Choice(f"{next(counter)}) Create gnosis safe", create_safe),
            Choice(f"{next(counter)}) Search NFTS2ME contracts", nfts2me_search_contracts),
            Choice(f"{next(counter)}) Mint NFT on NFTS2ME", mint_nft),
            Choice(f"{next(counter)}) Swap tokens to ETH", swap_tokens),
            Choice(f"{next(counter)}) Use Multiswap", swap_multiswap),
            Choice(f"{next(counter)}) Use custom routes", custom_routes),
            Choice(f"{next(counter)}) Use automatic routes", automatic_routes),
            Choice(f"{next(counter)}) Check transaction count", "tx_checker"),
            Choice(f"{next(counter)}) Exit", "exit"),
        ],
        qmark="⚙️ ",
        pointer="✅ "
    ).ask()
    if result == "exit":
        print("\n❤️ Subscribe to me – https://t.me/sybilwave\n")
        print("🤑 Donate me: 0x00000b0ddce0bfda4531542ad1f2f5fad7b9cde9")
        sys.exit()
    return result


def get_wallets():
    private_keys = get_private_keys()
    wallets = [
        {
            "id": _id,
            "key": key,
        } for _id, key in enumerate(private_keys, start=1)
    ]

    return wallets


async def run_module(module, account_id, key):
    await module(account_id, key)

    if REMOVE_WALLET:
        remove_wallet(key)

    await sleep(SLEEP_FROM, SLEEP_TO)


def _async_run_module(module, account_id, key):
    asyncio.run(run_module(module, account_id, key))


def main(module):
    if module == encrypt_privates:
        return encrypt_privates(force=True)
    if module == nfts2me_search_contracts:
        return asyncio.run(nfts2me_search_contracts())

    wallets = get_wallets()

    if RANDOM_WALLET:
        random.shuffle(wallets)

    with ThreadPoolExecutor(max_workers=QUANTITY_THREADS) as executor:
        for _, account in enumerate(wallets, start=1):
            executor.submit(
                _async_run_module,
                module,
                account.get("id"),
                account.get("key"),
            )
            time.sleep(random.randint(THREAD_SLEEP_FROM, THREAD_SLEEP_TO))


if __name__ == '__main__':

    logger.add('logs.txt', filter=filter_out_utils)  # todo

    module = get_module()
    if module == "tx_checker":
        get_tx_count()
    else:
        main(module)
