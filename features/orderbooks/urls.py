from django.urls import path

from features.orderbooks.views import RequestOrderBookView

app_name = 'orderbooks'

urlpatterns = [
    path('orderbooks/', RequestOrderBookView.as_view(), name='get_order_book')
]
