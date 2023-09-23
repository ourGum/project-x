from.views import index, welcome
from django.urls import path

urlpatterns = [
    path('', index),
    path('main/', welcome )
]