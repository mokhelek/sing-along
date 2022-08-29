from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import PostsSerializer
from main.models import *

from musixmatch import Musixmatch
 


# we make use of the 'GET' request if a user is just recieving information/data
@api_view(['GET'])
def getData(request):
    posts = Contact.objects.all()
    serializer = PostsSerializer(posts,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getLyricsData(request):
    #lyrics = {"name":"cassper","age":28,"song":"Doc Shebeleza"}
    musixmatch = Musixmatch("f5ef3ca46041df8004cf20333272dee2")
    lyrics = musixmatch.matcher_lyrics_get("Grenade", "Bruno Mars")
    return Response(lyrics)