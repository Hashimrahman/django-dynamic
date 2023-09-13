from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Italy'
    dest1.number = 8
    dest1.img = 'dest_1.png'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'France'
    dest2.number = 12
    dest2.img = 'dest_2.png'
    dest2.offer = False



    dest3 = Destination()
    dest3.name = 'America'
    dest3.number = 10
    dest3.img = 'dest_3.png'
    dest3.offer = True



    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests' : dests})