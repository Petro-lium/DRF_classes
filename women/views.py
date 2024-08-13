from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Women
from .serializers import WomenSerializer


class WomenViewSets(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

'''
class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
'''

#class WomenAPIView(generics.ListAPIView):
#    queryset = Women.objects.all()
#    serializer_class = WomenSerializer
