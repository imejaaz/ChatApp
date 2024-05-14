from django.urls import path
from . import consumers

websocket_urlpatterns=[

    path('social/', consumers.ChatConsumer.as_asgi()),

]