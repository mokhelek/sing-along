from django.shortcuts import render , redirect
from .forms import ContactForm

from musixmatch import Musixmatch

# Create your views here.
def index(request):
    if request.method != 'POST':
        form = ContactForm()
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
        
            form.save()
            
            return redirect('main:index' )  
    context = {"form":form}
    return render(request,"main/index.html" , context)

def getLyrics(request):
    musixmatch = Musixmatch("f5ef3ca46041df8004cf20333272dee2")
    lyrics = musixmatch.matcher_lyrics_get("Grenade", "Bruno Mars")
    return render(request,"main/getLyrics.html",{"lyrics":lyrics})

def MusicPlayer(request):
    
    return render(request,"main/music-player.html")
