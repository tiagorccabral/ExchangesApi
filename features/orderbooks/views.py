import requests
from django.shortcuts import render
from django.views import View
from my_secrets import secrets


class RequestOrderBookView(View):

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
