from django.shortcuts import render , redirect
from .forms import SignUpForm
from django.contrib.auth import login
# Create your views here.

#........................................................#

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('music_nation:home')
        else:
            message = 'Looks like a username with that email or password already exists'
            return render(request, 'registration/user_signup.html', {'form':form,'message':message})
    else:
        form = SignUpForm()
        return render(request, 'registration/user_signup.html', {'form':form})

#........................................................#
