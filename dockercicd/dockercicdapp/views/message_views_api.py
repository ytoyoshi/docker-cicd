from rest_framework.generics import RetrieveAPIView
from ..models import Message
from ..serializers import MessageSerializer
from django.shortcuts import get_object_or_404

class MessageDetailAPIView(RetrieveAPIView):
    serializer_class = MessageSerializer

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(Message, pk=pk)