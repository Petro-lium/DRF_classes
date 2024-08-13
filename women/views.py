from django.shortcuts import render
from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Womwn.objects.all()
    serializer_class = WomenSerializer


class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
