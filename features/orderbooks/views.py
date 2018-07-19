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
    BitstampEthereumsBid, BitstampEthereumsAsk)


class RequestOrderBookView(View):

    def get(self, request):

        # Set headers and urls
        # headers = {'Authorization': "ApiToken {}".format(secrets.BIT_COIN_TRADE_TOKEN)}
        bitcointradeurl = "https://api.bitcointrade.com.br/v1/public/BTC/orders"
        bitstrampurl = "https://www.bitstamp.net/api/v2/order_book/btcusd/"

        bitcointradeurlETH = "https://api.bitcointrade.com.br/v1/public/ETH/orders"
        bitstampurlETH = "https://www.bitstamp.net/api/v2/order_book/ethusd/"

        # Makes requisitions for bitcoins

        bitcointradeResponse = requests.get(bitcointradeurl).json()
        bitstampResponse = requests.get(bitstrampurl).json()

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

        # Return to same page that called
        return redirect(request.META['HTTP_REFERER'])


class RequestOrderBookGraphView(View):

    def get(self, request):

        # Sets interval to be greater or equal to the last 24 hours
        date_interval = timezone.now() - datetime.timedelta(days=1)

        # BitcoinTrade bid e asks de Bitcoin
        bitcointradeBid = BitcointradeBitcoinBid.objects.filter(saved_at__gte=date_interval).values()
        bitcointradeAsk = BitcointradeBitcoinAsk.objects.filter(saved_at__gte=date_interval).values()

        # BitcoinTrade bid e asks de Ethereum
        bitcointradeBidEth = BitcointradeEthereumsBid.objects.filter(saved_at__gte=date_interval).values()
        bitcointradeAskEth = BitcointradeEthereumsAsk.objects.filter(saved_at__gte=date_interval).values()

        # Bitstamp bid e asks de Bitcoin
        bitstampBid = BitstampBitcoinBid.objects.filter(saved_at__gte=date_interval).values()
        bitstampAsk = BitstampBitcoinAsk.objects.filter(saved_at__gte=date_interval).values()

        # Bitstamp bid e asks de Ethereums
        bitstampBidEth = BitstampEthereumsBid.objects.filter(saved_at__gte=date_interval).values()
        bitstampAskEth = BitstampEthereumsAsk.objects.filter(saved_at__gte=date_interval).values()

        # Return data to template
        return render(request, "features/orderbooks/orderbooks.html", {
            'bitcointradeBidBitcoin': bitcointradeBid,
            'bitcointradeAskBitcoin': bitcointradeAsk,
            'bitcointradeBidEthereum': bitcointradeBidEth,
            'bitcointradeAskEthereum': bitcointradeAskEth,
            'bitstampBidBitcoin': bitstampBid,
            'bitstampAskBitcoin': bitstampAsk,
            'bistampBidEthereum': bitstampBidEth,
            'bitstampAskEthereum': bitstampAskEth,
        })