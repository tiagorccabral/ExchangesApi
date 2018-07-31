import requests
from django.utils import timezone
from requests import RequestException

from orderbooks.models import BitcointradeBitcoinBid, BitcointradeBitcoinAsk, BitstampBitcoinBid, BitstampBitcoinAsk, \
    BitcointradeEthereumsBid, BitcointradeEthereumsAsk, BitstampEthereumsBid, BitstampEthereumsAsk, SpreadMaxBid, \
    BitstampEthBtcBid, BitstampEthBtcAsk, SpreadMaxAsk

MAX_WAIT_TIME = 5

FINISHED_WITH_SUCCESS = True
FINISHED_WITH_ERROR = False


def save_order_books():

    # Set headers and urls
    # headers = {'Authorization': "ApiToken {}".format(secrets.BIT_COIN_TRADE_TOKEN)}
    bitcointradeurl = "https://api.bitcointrade.com.br/v1/public/BTC/orders"
    bitstrampurl = "https://www.bitstamp.net/api/v2/order_book/btcusd/"
    bitstampethbtcurl = "https://www.bitstamp.net/api/v2/order_book/ethbtc/"

    bitcointradeurlETH = "https://api.bitcointrade.com.br/v1/public/ETH/orders"
    bitstampurlETH = "https://www.bitstamp.net/api/v2/order_book/ethusd/"

    # Makes requisitions for bitcoins
    try:
        bitcointradeResponse = requests.get(bitcointradeurl).json()
    except ConnectionError as e:
        print("A resposta de Bitcointrade Eth/Btc não funcionou. " + str(e) + "\n")
        return FINISHED_WITH_ERROR

    try:
        bitstampResponse = requests.get(bitstrampurl).json()
    except ConnectionError as e:
        print("A resposta de Bitcointrade Eth/Btc não funcionou. " + str(e) + "\n")
        return FINISHED_WITH_ERROR

    # Makes requisitions for eth/btc
    try:
        bitstampEthBtcResponse = requests.get(bitstampethbtcurl, timeout=MAX_WAIT_TIME).json()
    except ConnectionError as e:
        print("A resposta de Bitstamp Eth/Btc não funcionou. " + str(e) + "\n")
        return FINISHED_WITH_ERROR

    # Makes requisitions for ethereums
    bitcointradeETHResponse = requests.get(bitcointradeurlETH, timeout=MAX_WAIT_TIME)
    try:
        bitcointradeETHResponse = bitcointradeETHResponse.json()
    except ConnectionError as e:
        print("A resposta de Bitcointrade Eth não funcionou. " + str(e) + "\n")
        return FINISHED_WITH_ERROR

    bitstampurlETHResponse = requests.get(bitstampurlETH, timeout=MAX_WAIT_TIME)
    try:
        bitstampurlETHResponse = bitstampurlETHResponse.json()
    except ConnectionError as e:
        print("A resposta de Bitstamp Eth não funcionou. " + str(e) + "\n")
        return FINISHED_WITH_ERROR

    # Sets a current time for all the information collected by the responses
    current_date = timezone.localtime()

    BitcointradeBitcoinBid.objects.create(
        first_coin_value=bitcointradeResponse['data']['bids'][0]['unit_price'],
        second_coin_value=bitcointradeResponse['data']['bids'][1]['unit_price'],
        first_amount=bitcointradeResponse['data']['bids'][0]['amount'],
        second_amount=bitcointradeResponse['data']['bids'][1]['amount'],
        saved_at=current_date,
    )

    BitcointradeBitcoinAsk.objects.create(
        first_coin_value=bitcointradeResponse['data']['asks'][0]['unit_price'],
        second_coin_value=bitcointradeResponse['data']['asks'][1]['unit_price'],
        first_amount=bitcointradeResponse['data']['asks'][0]['amount'],
        second_amount=bitcointradeResponse['data']['asks'][1]['amount'],
        saved_at=current_date,
    )

    BitstampBitcoinBid.objects.create(
        first_coin_value=bitstampResponse['bids'][0][0],
        second_coin_value=bitstampResponse['bids'][1][0],
        first_amount=bitstampResponse['bids'][0][1],
        second_amount=bitstampResponse['bids'][1][1],
        saved_at=current_date,
    )

    BitstampBitcoinAsk.objects.create(
        first_coin_value=bitstampResponse['asks'][0][0],
        second_coin_value=bitstampResponse['asks'][1][0],
        first_amount=bitstampResponse['asks'][0][1],
        second_amount=bitstampResponse['asks'][1][1],
        saved_at=current_date,
    )

    BitcointradeEthereumsBid.objects.create(
        first_coin_value=bitcointradeETHResponse['data']['bids'][0]['unit_price'],
        second_coin_value=bitcointradeETHResponse['data']['bids'][1]['unit_price'],
        first_amount=bitcointradeETHResponse['data']['bids'][0]['amount'],
        second_amount=bitcointradeETHResponse['data']['bids'][1]['amount'],
        saved_at=current_date,
    )

    BitcointradeEthereumsAsk.objects.create(
        first_coin_value=bitcointradeETHResponse['data']['asks'][0]['unit_price'],
        second_coin_value=bitcointradeETHResponse['data']['asks'][1]['unit_price'],
        first_amount=bitcointradeETHResponse['data']['asks'][0]['amount'],
        second_amount=bitcointradeETHResponse['data']['asks'][1]['amount'],
        saved_at=current_date,
    )

    BitstampEthereumsBid.objects.create(
        first_coin_value=bitstampurlETHResponse['bids'][0][0],
        second_coin_value=bitstampurlETHResponse['bids'][1][0],
        first_amount=bitstampurlETHResponse['bids'][0][1],
        second_amount=bitstampurlETHResponse['bids'][1][1],
        saved_at=current_date,
    )

    BitstampEthereumsAsk.objects.create(
        first_coin_value=bitstampurlETHResponse['asks'][0][0],
        second_coin_value=bitstampurlETHResponse['asks'][1][0],
        first_amount=bitstampurlETHResponse['asks'][0][1],
        second_amount=bitstampurlETHResponse['asks'][1][1],
        saved_at=current_date,
    )

    BitstampEthBtcBid.objects.create(
        first_coin_value=bitstampEthBtcResponse['bids'][0][0],
        first_amount=bitstampEthBtcResponse['bids'][0][1],
        saved_at=current_date,
    )

    BitstampEthBtcAsk.objects.create(
        first_coin_value=bitstampEthBtcResponse['asks'][0][0],
        first_amount=bitstampEthBtcResponse['asks'][0][1],
        saved_at=current_date,
    )

    # Calculates the Max Spread for asks and saves it

    spread_result_ask = ((bitcointradeETHResponse['data']['asks'][0]['unit_price'] /
                          bitcointradeResponse['data']['asks'][0]['unit_price']) /
                         float(bitstampEthBtcResponse['asks'][0][0])) - 1.00

    SpreadMaxAsk.objects.create(
        spread=spread_result_ask,
        saved_at=current_date
    )

    # Calculates the Max Spread for bids and saves it

    spread_result_bid = ((bitcointradeETHResponse['data']['bids'][0]['unit_price'] /
                          bitcointradeResponse['data']['bids'][0]['unit_price']) /
                         float(bitstampEthBtcResponse['bids'][0][0])) - 1.00

    SpreadMaxBid.objects.create(
        spread=spread_result_bid,
        saved_at=current_date
    )

    return FINISHED_WITH_SUCCESS
