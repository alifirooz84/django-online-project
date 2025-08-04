from django.urls import path
from .views import phone_input

urlpatterns = [
    path('', phone_input, name='phone_input'),
]

