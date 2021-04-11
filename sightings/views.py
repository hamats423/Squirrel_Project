from django.shortcuts import render
from .models import Sightings

def index(request):
    sighting=Sightings.objects.all()
    context={
            'sighting':sighting,
            }
    
    return render(request, 'sightings/index.html', context)
