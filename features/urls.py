from django.urls import path, include

from features.views import HomeView

app_name = 'features'

urlpatterns = [
    path('', HomeView.as_view()),
    path('orderbooks/', include('features.orderbooks.urls'), name='get_order_book')
]
