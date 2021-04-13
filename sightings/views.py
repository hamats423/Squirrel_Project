from django.shortcuts import render
from .models import Sightings
from .forms import SightingsForm
from django .http import JsonResponse 
from django import forms
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.db.models import Count 

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
        form = SightingsForm()
        context = {
             'form':form,
             }
    return render(request, 'sightings/add_sightings.html', context)

def UpdateSquirrel(request, squirrel_pk):
    squirrel = Sightings.objects.get(unique_squirrel_id = squirrel_pk)
    form = SightingsForm(request.POST or None, instance = squirrel)
    context = {'form':form}
    
    if form.is_valid():  #check out if this works
        squirrels = form.save(commit = False)
        context = {'form':form}
        messages.success(request, 'Updated successfully!')
        return render(request, 'sightings/update_sightings.html', context) 

    else:
        context = {'form':form, 'error':'Update unsuccessful. Try again...'}
        return render(request, 'sightings/update_sightings.html',context)


def Stats(request):
    sq__age = Sightings.objects.values('Age').order_by('Age').annotate(age_count=Count('Age'))
    sq_running = Sightings.objects.values('Running').order_by('Running').annotate(running_count=Count('Running'))
    sq_eating = Sightings.objects.values('Eating').order_by('Eating').annotate(eating_count=Count('Eating'))
    sq_pfurcolor = Sightings.objects.values('PrimaryFurColor').order_by('PrimaryFurColor').annotate(primaryfurcolor_count=Count('PrimaryFurColor'))
    sq_kuks = Sightings.objects.values('Kuks').order_by('Kuks').annotate(kuks_count=Count('Kuks'))

    context = {
            'sq_age':sq_age,
            'sq_running':sq_running,
            'sq_eating':sq_eating,
            'sq_pfurcolor':sq_pfurcolor,
            'sq_kuks':sq_kuks,
            }
    return render(request, 'sightings/stats.html', context)

    









