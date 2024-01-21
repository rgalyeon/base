import asyncio

from modules import *


async def bridge_base(account_id, key):
    """
    Deposit from official bridge
    ______________________________________________________
    all_amount - bridge from min_percent to max_percent
    """

    min_amount = 0.001
    max_amount = 0.002
    decimal = 4

    all_amount = True

    min_percent = 5
    max_percent = 10

    base = Base(account_id, key, "ethereum")
    await base.deposit(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def withdraw_okx(_id, key):
    """
    Withdraw ETH from OKX. OKX support only ETH for Starknet chain
    ______________________________________________________
    min_amount - min amount (ETH)
    max_amount - max_amount (ETH)
    chains - ['zksync', 'arbitrum', 'linea', 'base', 'optimism']
    terminate - if True - terminate program if money is not withdrawn
    """
    token = 'ETH'
    chains = ['arbitrum', 'zksync', 'linea', 'base', 'optimism']

    min_amount = 0.0075
    max_amount = 0.01

    terminate = True

    okx_exchange = Okx(_id, key, chains)
    await okx_exchange.okx_withdraw(min_amount, max_amount, token, terminate)


async def bridge_orbiter(account_id, key, proxy):
    """
    Bridge from orbiter
    ______________________________________________________
    from_chain – ethereum, polygon_zkevm, arbitrum, optimism, zksync | Select one
    to_chain – ethereum, polygon_zkevm, arbitrum, optimism, zksync | Select one

    save_funds - how much eth save on the account (min and max, choose randomly)
    min_required_amount - минимальная требуемая сумма в сети, на которую будет реагировать модуль в eth
    """

    from_chains = ["arbitrum", "optimism", "base", "scroll", "linea"]
    to_chain = "zksync"

    min_amount = 0.005
    max_amount = 0.0051
    decimal = 4

    all_amount = False

    min_percent = 5
    max_percent = 10
    save_funds = [0.0006, 0.001]
    min_required_amount = 0.001

    orbiter = Orbiter(account_id, key, from_chains, min_required_amount)
    await orbiter.bridge(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent, save_funds)


async def wrap_eth(account_id, key):
    """
    Wrap ETH
    ______________________________________________________
    all_amount - wrap from min_percent to max_percent
    """

    min_amount = 0.001
    max_amount = 0.002
    decimal = 4

    all_amount = True

    min_percent = 5
    max_percent = 10

    base = Base(account_id, key, "base")
    await base.wrap_eth(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def unwrap_eth(account_id, key):
    """
    Unwrap ETH
    ______________________________________________________
    all_amount - unwrap from min_percent to max_percent
    """

    min_amount = 0.001
    max_amount = 0.002
    decimal = 4

    all_amount = True

    min_percent = 100
    max_percent = 100

    base = Base(account_id, key, "base")
    await base.unwrap_eth(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def swap_uniswap(account_id, key):
    """
    Make swap on Uniswap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, USDBC | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDBC"
    to_token = "ETH"

    min_amount = 0.001
    max_amount = 0.002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 1
    max_percent = 1

    uniswap = Uniswap(account_id, key)
    await uniswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_pancake(account_id, key):
    """
    Make swap on PancakeSwap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, USDBC | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "USDBC"

    min_amount = 0.001
    max_amount = 0.002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 1
    max_percent = 1

    pancake = Pancake(account_id, key)
    await pancake.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_woofi(account_id, key):
    """
    Make swap on WooFi
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, USDBC | Select one
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "USDBC"

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 1
    max_percent = 1

    woofi = WooFi(account_id, key)
    await woofi.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_baseswap(account_id, key):
    """
    Make swap on BaseSwap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, USDBC | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDBC"
    to_token = "ETH"

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 1
    max_percent = 1

    baseswap = BaseSwap(account_id, key)
    await baseswap.swap(from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent,
                        max_percent)


async def swap_alienswap(account_id, key):
    """
    Make swap on AlienSwap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, USDBC | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDC"
    to_token = "ETH"

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 100
    max_percent = 100

    alienswap = AlienSwap(account_id, key)
    await alienswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_odos(account_id, key):
    """
    Make swap on Odos
    ______________________________________________________
    from_token – Choose SOURCE token ETH, WETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, WETH, USDBC | Select one

    Disclaimer - If you use True for use_fee, you support me 1% of the transaction amount
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDBC"
    to_token = "ETH"

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 1
    max_percent = 1

    odos = Odos(account_id, key)
    await odos.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_inch(account_id, key):
    """
    Make swap on 1inch
    ______________________________________________________
    from_token – Choose SOURCE token ETH, WETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, WETH, USDBC | Select one

    Disclaimer - If you use True for use_fee, you support me 1% of the transaction amount
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "USDBC"

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 1
    max_percent = 1

    inch_dex = Inch(account_id, key)
    await inch_dex.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_openocean(account_id, key):
    """
    Make swap on OpenOcean
    ______________________________________________________
    from_token – Choose SOURCE token ETH, WETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, WETH, USDBC | Select one

    Disclaimer - If you use True for use_fee, you support me 1% of the transaction amount
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "USDBC"

    min_amount = 0.0001
    max_amount = 0.0001
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 1
    max_percent = 1

    openocean = OpenOcean(account_id, key)
    await openocean.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_xyswap(account_id, key):
    """
    Make swap on XYSwap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, WETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, WETH, USDBC | Select one

    Disclaimer - If you use True for use_fee, you support me 1% of the transaction amount
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "USDBC"

    min_amount = 0.0001
    max_amount = 0.0001
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 1
    max_percent = 1

    xyswap = XYSwap(account_id, key)
    await xyswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_maverick(account_id, key):
    """
    Make swap on Maverick
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, USDBC | Select one
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "USDBC"

    min_amount = 0.0001
    max_amount = 0.0001
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 1
    max_percent = 1

    maverick = Maverick(account_id, key)
    await maverick.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def bungee_refuel(account_id, key):
    """
    Make refuel on Bungee
    ______________________________________________________
    to_chain – Choose DESTINATION chain: BSC, OPTIMISM, GNOSIS, POLYGON, ZKSYNC, ARBITRUM, AVALANCHE, AURORA, ZK_EVM

    Disclaimer - The chain will be randomly selected
    ______________________________________________________
    random_amount – True - amount random from min to max | False - use min amount
    """

    chain_list = ["GNOSIS"]

    random_amount = False

    bungee = Bungee(account_id, key)
    await bungee.refuel(chain_list, random_amount)


async def stargate_bridge(account_id, key):
    """
    Stargate bridge ETH
    ______________________________________________________
    to_chain – Choose DESTINATION chain: arbitrum, optimism, linea

    Disclaimer - The chain will be randomly selected
    ______________________________________________________
    random_amount – True - amount random from min to max | False - use min amount
    """

    chain_list = ["arbitrum", "optimism"]

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    slippage = 1

    all_amount = True

    min_percent = 10
    max_percent = 10

    stargate = Stargate(account_id, key)
    await stargate.bridge(chain_list, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent)


async def deposit_aave(account_id, key):
    """
    Make deposit on Aave
    ______________________________________________________
    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """
    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    sleep_from = 5
    sleep_to = 24

    make_withdraw = True

    all_amount = True

    min_percent = 5
    max_percent = 10

    aave = Aave(account_id, key)
    await aave.deposit(
        min_amount, max_amount, decimal, sleep_from, sleep_to, make_withdraw, all_amount, min_percent, max_percent
    )


async def deposit_moonwell(account_id, key):
    """
    Make deposit on MoonWell
    ______________________________________________________
    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """
    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    sleep_from = 5
    sleep_to = 24

    make_withdraw = True

    all_amount = True

    min_percent = 5
    max_percent = 10

    moonwell = MoonWell(account_id, key)
    await moonwell.deposit(
        min_amount, max_amount, decimal, sleep_from, sleep_to, make_withdraw, all_amount, min_percent, max_percent
    )


async def bridge_nft(account_id, key):
    """
    Make mint NFT and bridge NFT on L2Telegraph
    """

    sleep_from = 5
    sleep_to = 20

    l2telegraph = L2Telegraph(account_id, key)
    await l2telegraph.bridge(sleep_from, sleep_to)


async def mint_mintfun(account_id, key):
    """
    Mint NFT on Mint.Fun
    ______________________________________________________
    Disclaimer - The Mint function should be called "mint", to make sure of this, look at the name in Rabby Wallet or in explorer
    """

    nft_contracts_data = {
        "0x69b69cc6e9f99c62a003fd9e143c126504d49dc2": 1,
        "0xea0b3e39ccd46d7F2B338D784De8519902f7E17E": 3,
    }

    mintfun = MintFun(account_id, key)
    await mintfun.mint(nft_contracts_data)


async def mint_zerius(account_id, key):
    """
    Mint + bridge Zerius NFT
    ______________________________________________________
    chains - list chains for random chain bridge: arbitrum, optimism, polygon, bsc, avalanche, zora
    Disclaimer - The Mint function should be called "mint", to make sure of this, look at the name in Rabby Wallet or in explorer
    """

    chains = ["zora"]

    sleep_from = 200
    sleep_to = 700

    zerius = Zerius(account_id, key)
    await zerius.bridge(chains, sleep_from, sleep_to)


async def mint_nft(account_id, key):
    """
    Mint NFT on NFTS2ME
    ______________________________________________________
    Specify contracts at data/nfts2me_contracts.json file or use nfts2me_search_contracts() module
    """

    contracts = ['0xe99BDeef1BfACBd8313015346C9E5f2CC03fC878']  # await parse_nfts2me_contracts(0, 200, 6000)
    print(contracts)
    minter = Minter(account_id, key)
    await minter.mint_nft(contracts)


async def mint_zkstars(account_id, key):
    """
    Mint ZkStars NFT
    """

    contracts = [
        "0x4c78c7d2f423cf07c6dc2542ac000c4788f03657",
        "0x657130a14e93731dfecc772d210ae8333303986c",
        "0x004416bef2544df0f02f23788c6ada0775868560",
        "0x39b06911d22f4d3191827ed08ae35b84f68843e4",
        "0x8a6a9ef84cd819a54eee3cf7cfd351d21ab6b5fe",
        "0x8fb3225d0a85f2a49714acd36cdcd96a7b2b7fbc",
        "0x91ad9ed35b1e9ff6975aa94690fa438efb5a7160",
        "0x32d8eeb70eab5f5962190a2bb78a10a5a0958649",
        "0xab62313752f90c24405287ad8c3bcf4c25c26e57",
        "0x6f562b821b5cb93d4de2b0bd558cc8e46b632a08",
        "0xb63159a26664a89abce783437fc17786af8bb46d",
        "0x7e6b32d7eecddb6be496f232ab9316a5bf9f4e17",
        "0xcb03866371fb149f3992f8d623d5aaa4b831e2fd",
        "0x78c85441f53a07329e2380e49f1870199f70cee1",
        "0x54c49cb80a0679e3217f86d891859b4e477b56c3",
        "0xad6f16f5ff3461c83d639901bae1fb2a8a68aa31",
        "0x023a7c97679f2c121a31bacf37292dabf7ab97e9",
        "0x5dabff127cad8d075b5cea7f795dcbae1ddf471d",
        "0xd3c6386362dabab1a30acc2c377d9ac2cc8b7b16",
        "0xed0407d6b84b2c86418cac16a347930b222b505c"
    ]

    mint_min = 1
    mint_max = 1

    mint_all = False

    sleep_from = 5
    sleep_to = 10

    zkkstars = ZkStars(account_id, key)
    await zkkstars.mint(contracts, mint_min, mint_max, mint_all, sleep_from, sleep_to)


async def swap_tokens(account_id, key):
    """
    SwapTokens module: Automatically swap tokens to ETH
    ______________________________________________________
    use_dex - Choose any dex: uniswap, pancake, woofi, baseswap, alienswap, maverick, odos, inch, xyswap, openocean
    """

    use_dex = [
        "uniswap", "pancake", "woofi", "baseswap",
        "alienswap", "maverick", "odos", "inch",
        "xyswap", "openocean"
    ]

    use_tokens = ["USDBC"]

    sleep_from = 300
    sleep_to = 600

    slippage = 1

    min_percent = 100
    max_percent = 100

    swap_tokens = SwapTokens(account_id, key)
    await swap_tokens.swap(use_dex, use_tokens, sleep_from, sleep_to, slippage, min_percent, max_percent)


async def swap_multiswap(account_id, key):
    """
    Multi-Swap module: Automatically performs the specified number of swaps in one of the dexes.
    ______________________________________________________
    use_dex - Choose any dex: uniswap, pancake, woofi, baseswap, alienswap, maverick, odos, inch, xyswap, openocean
    quantity_swap - Quantity swaps
    ______________________________________________________
    random_swap_token - If True the swap path will be [ETH -> USDBC -> USDBC -> ETH] (random!)
    If False the swap path will be [ETH -> USDBC -> ETH -> USDBC]
    """

    use_dex = ["uniswap", "pancake", "woofi", "baseswap", "odos"]

    min_swap = 1
    max_swap = 2

    sleep_from = 3
    sleep_to = 7

    slippage = 1

    random_swap_token = True

    min_percent = 5
    max_percent = 10

    multi = Multiswap(account_id, key)
    await multi.swap(
        use_dex, sleep_from, sleep_to, min_swap, max_swap, slippage, random_swap_token, min_percent, max_percent
    )


async def custom_routes(account_id, key):
    """
    BRIDGE:
        – bridge_base
        – bridge_orbiter
        – bungee_refuel
        – stargate_bridge
    WRAP:
        – wrap_eth
        – unwrap_eth
    DEX:
        – swap_uniswap
        – swap_pancake
        – swap_woofi
        – swap_baseswap
        – swap_alienswap
        – swap_maverick
        – swap_odos
        – swap_inch
        – swap_openocean
        – swap_xyswap
    LANDING:
        – deposit_aave
        – deposit_moonwell
        – withdraw_aave
        – withdraw_moonwell
    NFT/DOMAIN:
        – mint_zerius
        – mint_zkstars
        – mint_mintfun
        – mint_nft
    ANOTHER:
        – send_message
        – send_mail (Dmail)
        – bridge_nft
        – create_portfolio
        – swap_tokens
        – swap_multiswap
        – create_safe
        – mint_nft
    ______________________________________________________
    Disclaimer - You can add modules to [] to select random ones,
    example [module_1, module_2, [module_3, module_4], module 5]
    The script will start with module 1, 2, 5 and select a random one from module 3 and 4

    You can also specify None in [], and if None is selected by random, this module will be skipped

    You can also specify () to perform the desired action a certain number of times
    example (send_mail, 1, 10) run this module 1 to 10 times
    """

    use_modules = [
        [bridge_nft, deposit_aave, None],
        (bridge_nft, 1, 3),
    ]

    sleep_from = 10
    sleep_to = 20

    random_module = True

    routes = Routes(account_id, key)
    await routes.start(use_modules, sleep_from, sleep_to, random_module)


async def automatic_routes(account_id, key):
    """
    Модуль автоматически генерирует пути по которому пройдет кошелек,
    меняя вероятности выбрать тот или иной модуль для каждого кошелька

    Parameters
    ----------
    transaction_count - количество транзакций (не обязательно все выполнятся, модули могут пропускаться)
    cheap_ratio - от 0 до 1, доля дешевых транзакций при построении маршрута
    cheap_modules - список модулей, которые будут использоваться в качестве дешевых
    expensive_modules - список модулей, которые будут использоваться в качестве дорогих
    -------

    """

    transaction_count = 25
    cheap_ratio = 1.0

    sleep_from = 30
    sleep_to = 60

    cheap_modules = [send_mail, create_safe, mint_zkstars, mint_nft]
    expensive_modules = [swap_multiswap, deposit_aave, deposit_moonwell, create_portfolio, mint_zerius]

    routes = Routes(account_id, key)
    await routes.start_automatic(transaction_count, cheap_ratio, sleep_from, sleep_to, cheap_modules, expensive_modules)


async def nfts2me_search_contracts():
    """
    Module for searching nfts collections created in the nfts2me service.
    If you do not want to search for smart contracts for the mint_nfts2me module,
    you can run this module and it will add the addresses of contracts to the config by itself.
    ______________________________________________________
    mint_price - mint price of the searched contract
    min_total_supply - minimum supply of the collection
    search_limit - The maximum number of recent transactions to search through. Max: 10000
    """
    mint_price = 0
    min_total_supply = 100
    search_limit = 9000

    await find_and_update_nfts2me_contracts(mint_price, min_total_supply, search_limit)


#########################################
########### NO NEED TO CHANGE ###########
#########################################
async def send_mail(account_id, key):
    dmail = Dmail(account_id, key)
    await dmail.send_mail()


async def withdraw_aave(account_id, key):
    aave = Aave(account_id, key)
    await aave.withdraw()


async def withdraw_moonwell(account_id, key):
    moonwell = MoonWell(account_id, key)
    await moonwell.withdraw()


async def send_message(account_id, key):
    l2telegraph = L2Telegraph(account_id, key)
    await l2telegraph.send_message()


async def create_portfolio(account_id, key):
    rai = Rai(account_id, key)
    await rai.create()


async def create_safe(account_id, key):
    gnosis_safe = GnosisSafe(account_id, key)
    await gnosis_safe.create_safe()


def get_tx_count():
    asyncio.run(check_tx())


def start_encrypt():
    encrypt_privates(force=True)
