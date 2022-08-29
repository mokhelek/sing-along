from django.urls import path
from .import views


urlpatterns = [
    path("",views.getData),
    path("lyrics/",views.getLyricsData),
]