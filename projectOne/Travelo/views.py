from django.shortcuts import render

from .models import Destination
# Create your views here.

def index(request):

    #We don't have to create objects one by one now, We have a database!!!

    # dest1 = Destination()
    # dest1.name = 'Durban'
    # dest1.desc = 'Retsene we are within!!'
    # dest1.price = 800
    # dest1.image = '1.png'

    # dest2 = Destination()
    # dest2.name = 'CapeTown'
    # dest2.desc = 'Hakuna Matata!!'
    # dest2.price = 900
    # dest2.image = '2.png'

    # dest3 = Destination()
    # dest3.name = 'Johannesburg'
    # dest3.desc = 'Dintsang baba!!'
    # dest3.price = 850
    # dest3.image = '3.png'


    # #A list of objects
    # dests = [dest1, dest2, dest3]

    dests = Destination.objects.all()

    return render(request, "index.html", {'dests':dests})