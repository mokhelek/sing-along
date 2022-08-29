from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Album, Song

class NewAlbum(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('album_name','album_genre','album_logo',)



class NewSong(forms.ModelForm):

    class Meta:
        model = Song
        fields = ('song_name','song_file',)
