
from django.urls import path, include, re_path
from . import views as music_nation_views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/user_login.html'), name="login"),
    path('signup/', music_nation_views.signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]