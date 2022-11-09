from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import SignUpForm, RoomCreationForm
from .models import Room, Message, MessageStatus


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mainpage')
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})


@login_required
def rooms(request):
    if request.method == 'POST':
        form = RoomCreationForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = RoomCreationForm()

    rooms = Room.objects.all()
    return render(request, 'base.html', {'rooms': rooms, 'form': form})


@login_required
def room(request, slug):
    # user = request.user.id

    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)

    return render(request, 'room.html', {'room': room, 'messages': messages})
