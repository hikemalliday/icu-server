from rest_framework import serializers
from .models import DiscordMessage


class DiscordMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscordMessage
        fields = '__all__'
    # Debug prints
    def __init__(self, *args, **kwargs):
        incoming_data = kwargs.get("data")
        print("Incoming request data in serializer:", incoming_data)
        super().__init__(*args, **kwargs)

    