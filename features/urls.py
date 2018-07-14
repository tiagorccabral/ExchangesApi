from django.urls import path

from features.views import HomeView

app_name = 'features'

urlpatterns = [
    path('', HomeView.as_view())
]
