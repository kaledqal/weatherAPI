from django.urls import path
from weather import views

urlpatterns = [
    path('weather', views.WeatherAppView.as_view()),
]