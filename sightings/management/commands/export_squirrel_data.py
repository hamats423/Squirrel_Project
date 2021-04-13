from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sightings
import csv, os, sys
from django.db.models import get_model
class Command(BaseCommand):
        help = "Export data to .csv file"
        args = '[squirrel_tracker.Sightings]'
        def handle(self,*app_labels,**kwargs):
                app_name, model_name = app_labels[0].split('.')
                model = get_model('sightings','Sightings')
                field_names = [f.name for f in model._meta.fields]
                writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
                writer.writerow(field_names)
                for instance in model.objects.all():
                        writer.writerow([unicode(getattr(instance, f)).encode('utf-8') for f in field_names])

