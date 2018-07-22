from django.urls import path, include

from features.views import HomeView
from patches import routers
from features.orderbooks.urls import router as router_orderbooks

app_name = 'features'

router = routers.DefaultRouter()

router.extend(router_orderbooks)

urlpatterns = [
    path('', HomeView.as_view()),
    path('orderbooks/', include('features.orderbooks.urls'), name='get_order_book')
]

urlpatterns = urlpatterns + router.urls
