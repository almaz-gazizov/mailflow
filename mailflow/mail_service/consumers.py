import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ProgressConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        async_to_sync(self.channel_layer.group_add)(
            'progress', self.channel_name
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'progress', self.channel_name
        )

    def send_progress(self, event):
        progress = event['progress']
        message = event.get('message', None)
        self.send(text_data=json.dumps(
            {'progress': progress, 'message': message}
        ))
