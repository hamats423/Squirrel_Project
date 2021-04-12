from django.shortcuts import render
from .models import Sightings
from .forms import SightingsForm
from django .http import JsonResponse 
from django import forms

def index(request):
    sightings=Sightings.objects.all()
    context={
            'sightings':sightings,
            }
    return render(request, 'sightings/index.html', context)


def AddSquirrel(request):
    if request.method == 'POST':
         form = SightingsForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('/sightings/')   #check later
        
         else:
             form = Form()
             context = {'form':form,}
             return render(request, '', context) #make html


def UpdateSquirrel(request, squirrel_pk):
    squirrel = Sightings.objects.get(unique_squirrel_id = squirrel_pk)
    form = SightingsForm(request.POST or None, instance = squirrel)
    context = {'form':form}
    
    if form.is_valid():  #check out if this works
        squirrels = form.save(commit = False)
        context = {'form':form}
        return render (request, 'sightings/update_sightings.html', context) 

    else:
        return render(request, 'sightings/update_sightings.html', context)


def Stats(request):
    pass









