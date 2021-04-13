from django.shortcuts import render
from sightings.models import Sightings
from django.http import HttpResponse
import random 

def map(request):
    squirrel_data = random.sample(range(Sightings.objects.count()),100)
    sightings = [Sightings.objects.all()[item] for item in squirrel_data]
    context = {
            'sightings': sightings,
    }
    return render(request, 'sightings/map.html', context)



