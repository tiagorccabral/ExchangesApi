import datetime
import requests
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from my_secrets import secrets
from orderbooks.models import (
    BitcointradeBitcoinBid, BitcointradeBitcoinAsk,
    BitstampBitcoinBid, BitstampBitcoinAsk,
    BitcointradeEthereumsBid, BitcointradeEthereumsAsk,
    BitstampEthereumsBid, BitstampEthereumsAsk, BitstampEthBtcBid, BitstampEthBtcAsk, SpreadMaxAsk, SpreadMaxBid)


class RequestOrderBookView(View):

    def get(self, request):

        # Set headers and urls
        # headers = {'Authorization': "ApiToken {}".format(secrets.BIT_COIN_TRADE_TOKEN)}
        bitcointradeurl = "https://api.bitcointrade.com.br/v1/public/BTC/orders"
        bitstrampurl = "https://www.bitstamp.net/api/v2/order_book/btcusd/"
        bitstampethbtcurl = "https://www.bitstamp.net/api/v2/order_book/ethbtc/"

        bitcointradeurlETH = "https://api.bitcointrade.com.br/v1/public/ETH/orders"
        bitstampurlETH = "https://www.bitstamp.net/api/v2/order_book/ethusd/"

        # Makes requisitions for bitcoins

        bitcointradeResponse = requests.get(bitcointradeurl).json()
        bitstampResponse = requests.get(bitstrampurl).json()

        # Makes requisitions for eth/btc

        bitstampEthBtcResponse = requests.get(bitstampethbtcurl).json()

        # Makes requisitions for ethereums

        bitcointradeETHResponse = requests.get(bitcointradeurlETH).json()
        bitstampurlETHResponse = requests.get(bitstampurlETH).json()

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

        # Return to same page that called
        return redirect(request.META['HTTP_REFERER'])


class RequestOrderBookGraphView(View):

    def get(self, request):

        # Sets interval to be greater or equal to the last 24 hours
        date_interval = timezone.now() - datetime.timedelta(days=1)

        # BitcoinTrade bid e asks de Bitcoin
        bitcointrade_bid_btc = BitcointradeBitcoinBid.objects.filter(saved_at__gte=date_interval).values()
        bitcointrade_ask_btc = BitcointradeBitcoinAsk.objects.filter(saved_at__gte=date_interval).values()

        # BitcoinTrade bid e asks de Ethereum
        bitcointrade_bid_eth = BitcointradeEthereumsBid.objects.filter(saved_at__gte=date_interval).values()
        bitcointrade_ask_eth = BitcointradeEthereumsAsk.objects.filter(saved_at__gte=date_interval).values()

        # Bitstamp bid e asks de Bitcoin
        bitstamp_bid_btc = BitstampBitcoinBid.objects.filter(saved_at__gte=date_interval).values()
        bitstamp_ask_btc = BitstampBitcoinAsk.objects.filter(saved_at__gte=date_interval).values()

        # Bitstamp bid e asks de Ethereums
        bitstamp_bid_eth = BitstampEthereumsBid.objects.filter(saved_at__gte=date_interval).values()
        bitstamp_ask_eth = BitstampEthereumsAsk.objects.filter(saved_at__gte=date_interval).values()

        # Bitstamp bid e asks Eth/Btc
        bitstamp_bid_eth_btc = BitstampEthBtcBid.objects.filter(saved_at__gte=date_interval).values()
        bitstamp_ask_eth_btc = BitstampEthBtcAsk.objects.filter(saved_at__gte=date_interval).values()

        # Spread max bid e asks
        spread_max_ask = SpreadMaxAsk.objects.filter(saved_at__gte=date_interval).values()
        spread_max_bid = SpreadMaxBid.objects.filter(saved_at__gte=date_interval).values()

        # Return data to template
        return render(request, "features/orderbooks/orderbooks.html", {
            'bitcointradeBidBitcoin': bitcointrade_bid_btc,
            'bitcointradeAskBitcoin': bitcointrade_ask_btc,
            'bitcointradeBidEthereum': bitcointrade_bid_eth,
            'bitcointradeAskEthereum': bitcointrade_ask_eth,
            'bitstampBidBitcoin': bitstamp_bid_btc,
            'bitstampAskBitcoin': bitstamp_ask_btc,
            'bistampBidEthereum': bitstamp_bid_eth,
            'bitstampAskEthereum': bitstamp_ask_eth,
            'bitstampEthBtcBid': bitstamp_bid_eth_btc,
            'bitstampEthBtcAsk': bitstamp_ask_eth_btc,
            'spreadMaxAsk': spread_max_ask,
            'spreadMaxBid': spread_max_bid,
        })
