from graphene import relay

class CustomNode(relay.Node):
    class Meta:
        name = 'Node'