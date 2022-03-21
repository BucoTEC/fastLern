from unicodedata import name
from django.urls import path
from .views import home, room

urlpatterns =[
    path('home/',home, name="home" ),
    path('room/',room, name="room" )

]
