import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        # 建立 websocket连接 (进入指定url 会自动建立连接)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        # 断开 websocket连接 (关闭浏览器会自动断开连接)
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        # 接收消息 并把接受到的消息推送消息到聊天室储存区
        # 紧接着调用方法 chat_message(self, event) 推送储存区的消息
        text_data_json = json.loads(text_data)
        user_id = text_data_json['user_id']
        message = text_data_json.get('message')
        if message:
            async_to_sync(self.channel_layer.group_send)(

                self.room_group_name,
                {
                    'type': 'chat_message',
                    'user_id': user_id,
                    'message': message,
                }
            )

    def chat_message(self, event):
        # 把聊天室储存区的消息推送到所有进入聊天室中的浏览器上
        if event.get('message'):
            user_id = event['user_id']
            message = event['message']
            self.send(text_data=json.dumps({
                'user_id': user_id,
                'message': message,
            }))