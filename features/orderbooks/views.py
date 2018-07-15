import requests
from django.shortcuts import render
from django.views import View


class RequestOrderBookView(View):

    def get(self, request):
        response = requests.get("https://www.bitstamp.net/api/v2/order_book/btcusd/").json()
        return render(request, "features/orderbooks/orderbooks.html", {'response': response})
