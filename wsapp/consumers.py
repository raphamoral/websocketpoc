import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import DataHistory
from .utils import fetch_items

class DataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        try:
            payload = json.loads(text_data or "{}")
        except json.JSONDecodeError:
            payload = {}
        api_type = int(payload.get("api_type", 1))
        items = fetch_items(api_type)
        for item in items:
            DataHistory.objects.create(api_type=api_type, data=item)
        await self.send(text_data=json.dumps(items))
