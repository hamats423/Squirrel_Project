from django.shortcuts import render
from .models import Sightings

def index(request):
    sightings=Sightings.objects.all()
    context={
            'sightings':sightings,
            }
    
    return render(request, 'sightings/index.html', context)
