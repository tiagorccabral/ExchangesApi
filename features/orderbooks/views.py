import datetime
import requests
from django.shortcuts import render, redirect
from django.views import View
from my_secrets import secrets
from orderbooks.models import (
    BitcointradeBitcoinBid, BitcointradeBitcoinAsk,
    BitstampBitcoinBid, BitstampBitcoinAsk,
    BitcointradeEthereumsBid, BitcointradeEthereumsAsk
)


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
        current_date = datetime.datetime.now()

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
            first_coin_value=bitcointradeResponse['data']['asks'][0]['unit_price'],
            second_coin_value=bitcointradeResponse['data']['asks'][1]['unit_price'],
            first_amount=bitcointradeResponse['data']['asks'][0]['amount'],
            second_amount=bitcointradeResponse['data']['asks'][1]['amount'],
            saved_at=current_date,
        )

        # Return to same page that called
        return redirect(request.META['HTTP_REFERER'])


class RequestOrderBookGraphView(View):

    def get(self, request):

        # Set headers and urls
        # headers = {'Authorization': "ApiToken {}".format(secrets.BIT_COIN_TRADE_TOKEN)}
        bitcointradeurl = "https://api.bitcointrade.com.br/v1/public/BTC/orders"
        bitstrampurl = "https://www.bitstamp.net/api/v2/order_book/btcusd/"

        # Makes requisitions
        bitcointradeResponse = requests.get(bitcointradeurl).json()
        bitstampResponse = requests.get(bitstrampurl).json()


        # Return data to template
        return render(request, "features/orderbooks/orderbooks.html", {
            'bitstampResponse': bitstampResponse,
            'bitcointradeResponse': bitcointradeResponse
        })