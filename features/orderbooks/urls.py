from django.urls import path
from rest_framework.routers import SimpleRouter

from features.orderbooks.views import RequestOrderBookView, RequestOrderBookGraphView, SaveDataView

app_name = 'orderbooks'

router = SimpleRouter()

urlpatterns = [
    path('', RequestOrderBookGraphView.as_view(), name='get_order_book'),
    path('create-order-book/', RequestOrderBookView.as_view(), name='post_order_book'),
    path('save-data', SaveDataView)
]

urlpatterns += router.urls
