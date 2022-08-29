from django.urls import path
from .import views

app_name = "main"
urlpatterns = [
    path("",views.index,name="index"),
    path("getLyrics/",views.getLyrics,name="getLyrics"),
    path("music-player/",views.MusicPlayer,name="music-player"),
]
