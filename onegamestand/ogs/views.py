from django.http import response
from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'index.html')

def createroom(request):
    return render(request, 'createroom.html')

def a_room(request):
    rname=request.GET['rname']
    game=request.GET['game']
    time=request.GET['time']
    fav_language=request.GET['fav_language']
    people=request.GET['people']
    
    return render(request, 'a_room.html', {
        'rname':rname,
        'game':game,
        'time':time,
        'fav_language':fav_language,
        'people':people,
       
        })

def username(request):
    name=request.GET['name']
    return render(request, 'rooms.html', {'name':name})