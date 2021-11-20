from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def rooms(request):
    return render(request, 'rooms.html')

def createroom(request):
    return render(request, 'createroom.html')

def a_room(request):
    return render(request, 'a_room.html')