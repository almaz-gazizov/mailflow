from django.urls import re_path

from mail_service.consumers import ProgressConsumer

websocket_urlpatterns = [
    re_path(r'ws/progress/$', ProgressConsumer.as_asgi()),
]
