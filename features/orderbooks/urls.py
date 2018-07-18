from django.urls import path

from features.orderbooks.views import RequestOrderBookView, RequestOrderBookGraphView

app_name = 'orderbooks'

urlpatterns = [
    path('', RequestOrderBookGraphView.as_view(), name='get_order_book'),
    path('create-order-book/', RequestOrderBookView.as_view(), name='post_order_book')
]
