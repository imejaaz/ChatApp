from channels.consumer import SyncConsumer

class ChatConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print('connected')
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        self.send({
            "type": "websocket.send",
            "text": event["text"],
        })