from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from time import sleep
import asyncio

class ChatConsumer(AsyncWebsocketConsumer):


    async def connect(self):
       await self.accept()
       
       print('connection created')
       
    

    async def receive(self, text_data=None, bytes_data=None):
        
        for i in range (30):
            await self.send(text_data="Hello world!")
            await asyncio.sleep(1)
  

    async def disconnect(self, close_code):
        print('connection has beed ended')