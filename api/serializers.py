from rest_framework import serializers
from main.models import *
from music_nation.models import *

"""
We serialize data so that the data from the model
can be in a format that the django rest framwork can
work with

"""

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        
    