from rest_framework import serializers
from .models import *

class singerserializer(serializers.ModelSerializer):
    song = serializers.StringRelatedField(many = True,read_only=True)

    class Meta:
        model = singer
        fields = ['id','name','gender','song']

class songerserializer(serializers.ModelSerializer):
    class Meta:
        model = song
        fields = ['id','title','singer','duration']