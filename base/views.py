from multiprocessing import context
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id':1,'name':'python'},
    {'id':2,'name':'javaScript'},
    {'id':3,'name':'goLang'},

]

def home(request):
    context ={
        'rooms':rooms
    }
    return render(request, 'home.html', context)

def room(request):
    
    return render(request, 'room.html', )
