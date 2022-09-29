from django.shortcuts import render
from .serializers import MyaccountSerializer
from rest_framework import viewsets
from .models import Myaccount
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class MyaccountView(viewsets.ModelViewSet):
    queryset=Myaccount.objects.all()
    serializer=MyaccountSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]