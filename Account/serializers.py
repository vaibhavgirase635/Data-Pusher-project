from rest_framework import serializers
from .models import Myaccount
class MyaccountSerializer(serializers.Serializer):
    class Meta:
        model=Myaccount
        fields=['email','accountid','name']
        