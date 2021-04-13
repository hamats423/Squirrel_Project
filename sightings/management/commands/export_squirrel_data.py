from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sightings
import csv, os, sys
from django.apps import apps

class Command(BaseCommand):
        help = "Export data to .csv file"
        
        def add_arguments(self, parser):
            parser.add_argument('path', type=str)

        def handle(self,*app_labels,**kwargs):
        
            path_to_file = kwargs['path']
            model = apps.get_model('sightings','Sightings')
            field_names = [f.name for f in model._meta.fields]
            writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
            writer.writerow(field_names)
            for instance in model.objects.all():
                    writer.writerow([(getattr(instance, f)) for f in field_names])

