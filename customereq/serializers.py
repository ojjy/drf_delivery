from rest_framework import serializers
from .models import Customereq

class CustomereqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customereq
        fields = ['sender_name', 'sender_address', 'sender_detailAddress', 'sender_extraAddress', 'sender_postcode',
                  'receiver_name', 'receiver_address', 'receiver_detailAddress', 'receiver_extraAddress',
                  'receiver_postcode', 'items', 'request_message']