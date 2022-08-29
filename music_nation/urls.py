from django.urls import path, include, re_path
from . import views as music_nation_views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'music_nation'
urlpatterns = [
    #home /
    path('', music_nation_views.home, name='home'),
    path('playing', music_nation_views.playing, name='playing'),

    #profile_detail /@username/
    path('@<str:username>/', music_nation_views.profile_detail, name='profile_detail'),

    #add new album /@username/add
    path('@<str:username>/add/', music_nation_views.add_album, name='add_album'),

    #album's detail page /@username/album/album_name
    path('@<str:username>/album/<str:album>/', music_nation_views.album_detail, name='album_detail'),

    # login the user /login/
    path('login/', LoginView.as_view(template_name='music_nation/user_login.html'), name="login"),

    #delete album /@username/album/album_name/delete
    path('@<str:username>/album/<str:album>/delete/', music_nation_views.delete_album, name='delete_album'),

    #add songs to the albums
    path('@<str:username>/album/<str:album>/add/', music_nation_views.add_song, name='add_song'),

    #logout the current user
    path('logout/', LogoutView.as_view(), name='logout'),
]
#path('link', view, name='', kwargs={})
#re_path(r'regex', view, name='', kwargs={})
