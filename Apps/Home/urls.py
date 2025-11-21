
from Apps.Home.views import HomeView
from django.urls import path

app_name='home'
urlpatterns = [
    path('', HomeView.as_view(), name='homeapp'),
    
]