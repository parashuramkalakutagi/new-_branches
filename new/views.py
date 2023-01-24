from django.shortcuts import render
from rest_framework import viewsets
from .serializers import singerserializer,songerserializer
from .models import singer,song
# Create your views here.

class singer_details(viewsets.ModelViewSet):
    queryset = singer.objects.all()
    serializer_class = singerserializer

class song_deatils(viewsets.ModelViewSet):
    queryset = song.objects.all()
    serializer_class = songerserializer