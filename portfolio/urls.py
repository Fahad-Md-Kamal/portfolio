
from django.urls import path

from .views import portfolioView


app_name = 'portfolio'

urlpatterns = [
    path('', portfolioView, name='Portfolio-view'),
]
