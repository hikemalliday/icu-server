from rest_framework import viewsets
from rest_framework_api_key.permissions import HasAPIKey
from .serializers import DiscordMessageSerializer
from rest import models

class DiscordMessageViewSet(viewsets.ModelViewSet):
    """
    Viewset for accepting Discord Message POST's from the client
    """
    queryset = models.DiscordMessage.objects.all()
    serializer_class = DiscordMessageSerializer
    permission_classes = [HasAPIKey]
    
    # Debug logs
    def update(self, request, *args, **kwargs):
        print("Incoming update data:", request.data)
        return super().update(request, *args, **kwargs)
    
    # Debug logs
    def create(self, request, *args, **kwargs):
        print("Raw request body:", request.body)
        print("Request data (parsed):", request.data)
        return super().create(request, *args, **kwargs)


