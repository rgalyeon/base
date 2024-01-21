# RANDOM WALLETS MODE
RANDOM_WALLET = True  # True/False

# removing a wallet from the list after the job is done
REMOVE_WALLET = False

SLEEP_FROM = 500  # Second
SLEEP_TO = 1000  # Second

QUANTITY_THREADS = 1

THREAD_SLEEP_FROM = 5
THREAD_SLEEP_TO = 5

# GWEI CONTROL MODE
CHECK_GWEI = False  # True/False
MAX_GWEI = 20
REALTIME_GWEI = True  # если включен, то будет считывать гвей из файла realtime_settings.json в реалтайме

# Рандомизация гвея. Если включен режим, то максимальный гвей будет выбираться из диапазона
RANDOMIZE_GWEI = True  # if True, max Gwei will be randomized for each wallet for each transaction
MAX_GWEI_RANGE = [24, 27]

GAS_SLEEP_FROM = 500
GAS_SLEEP_TO = 2000

GAS_PRIORITY_FEE = {
    "ethereum": 0.05,
    "polygon": 40,
    "arbitrum": 0.1,
    "base": 0.0001,
    "zksync": 0.25,
}

GAS_MULTIPLIER = 1.3

# RETRY MODE
RETRY_COUNT = 3

# INCH API KEY
INCH_API_KEY = ""
