from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sightings
import csv, os
import datetime


class Command(BaseCommand):

    help = "Read data - note: non-mandatory fields have been assigned arbitrary features"
    
    def __enter__(self):
         return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finalize()

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)
    
    def handle(self, *args, **kwargs):
        path_to_file = kwargs['path']
        with open(path_to_file, 'r') as csvFile:
            reader = csv.reader(csvFile)
            next(reader)
            Sightings.objects.all().delete()
            for i in list(reader):
                try:
                    #date =  i[5][4:] + '-' + i[5][0:2] + '-' + i[5][2:4]
                    added_sightings = Sightings(
                            Latitude = float(i[1]),
                            Longitude = float(i[0]),
                            UniqueSquirrelID = i[2],
                            Shift = i[4],
                            Date = f"{i[5][4:]}-{i[5][:2]}-{i[5][2:4]}",
                            Age = i[7],
                            Primary_Fur_Color = i[8],
                            Location = i[12],
                            SpecificLocation = i[14],
                            Running = str(i[15]).lower(),
                            Chasing = str(i[16]).lower(),
                            Climbing = str(i[17]).lower(),
                            Eating = str(i[18]).lower(),
                            Foraging = str(i[19]).lower(),
                            OtherActivities = i[20],
                            Kuks = str(i[21]).lower(),
                            Quaas = str(i[22]).lower(),
                            Moans = str(i[23]).lower(),
                            TailFlags = str(i[24]).lower(),
                            TailTwitches = str(i[25]).lower(),
                            Approaches = str(i[26]).lower(),
                            Indifferent = str(i[27]).lower(),
                            RunsFrom = str(i[28]).lower(),
                    )   
                    added_sightings.save()
                except:
                    return "Sorry, something went nuts!"

