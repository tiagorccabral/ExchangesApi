import requests
from django.shortcuts import render
from django.views import View
from my_secrets import secrets


class RequestOrderBookView(View):

    def get(self, request):

        # Set headers and urls
        headers = {'Authorization': "ApiToken {}".format(secrets.BIT_COIN_TRADE_TOKEN)}
        bitcointradeurl = "https://api.bitcointrade.com.br/v1/market?currency=BTC"
        bitstrampurl = "https://www.bitstamp.net/api/v2/order_book/btcusd/"

        # Makes requisitions
        bitstampResponse = requests.get(bitstrampurl).json()
        bitcointradeResponse = requests.get(bitcointradeurl, headers=headers)

        # Return data to template
        return render(request, "features/orderbooks/orderbooks.html", {
            'bitstampResponse': bitstampResponse,
            'bitcointradeResponse': bitcointradeResponse
        })
