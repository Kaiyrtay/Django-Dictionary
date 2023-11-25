from django.urls import path
from . import views

app_name = "dictionary"

urlpatterns = [
    path('', views.homeView, name='home'),
    path('search', views.searchView, name='search'),
]
