from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter

import chat.routing
#ProtocolTypeRouter： ASIG支持多种不同的协议，
#在这里可以指定特定协议的路由信息，我们只使用了websocket协议，这里只配置websocket即可

#AuthMiddlewareStack： django的channels封装了django的auth模块，
#使用这个配置我们就可以在consumer中通过下边的代码获取到用户的信息


def connect(self):
    self.user = self.scope["user"]
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})