from django.urls import re_path
from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/room/(?P<room_name>|w+)/$',ChatConsumer)
]