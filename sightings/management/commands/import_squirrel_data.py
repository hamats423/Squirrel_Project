from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sightings
import csv
import os
class Command(BaseCommand):
        help = "Read data - note: non-mandatory fields have been assigned arbitrary features"
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.model_name = Sightings

        def add_arg(self, parser):
                parser.add_argument('path_to_file', type = str)
        def handle(self, *args, **options):
                path = options['path_to_file']
                try:
                        with open(path, 'r') as csv_file:
                                csv_reader = csv.reader(csv_file)
                                for row in csv_reader:
                                    if row[7] is not None:
                                        age = row[7]
                                    else:
                                        age = "Juvenile"
                                    if row[8] is not None:
                                        primary = row[8]
                                    else:
                                        primary = "Gray"
                                    if row[12] is not None:
                                        location=row[12]
                                    else:
                                        location ="Ground Plane"
                                    if row[14] is not None:
                                        specificlocation = row[14]
                                    else:
                                        specificlocation = "on tree stump"
                                    
                                    if row[20] is not None:
                                        otheractivities=row[20]
                                    else:
                                        otheractivities="grooming"

                                    added_sighting=Sightings(
                                                Latitude =float(row[0]),
                                                Longitude = float(row[1]),
                                                UniqueSquirrelID=row[2],
                                                Shift = row[4],
                                                Date = f"{row[5][4:]}-{row[5][:2]}-{row[5][2:4]}",
                                                Age = age,
                                                PrimaryFurColor=primary,
                                                Location=location,
                                                SpecificLocation=specificlocation,
                                                Running=row[15].lower(),
                                                Chasing=row[16].lower(),
                                                Climbing=row[17].lower(),
                                                Eating=row[18].lower(),
                                                Foraging=row[19].lower(),
                                                OtherActivities=otheractivities,
                                                Kuks=row[21].lower(),
                                                Quaas=row[22].lower(),
                                                Moans=row[23].lower(),
                                                TailFlags=row[24].lower(),
                                                TailTwitches=row[25].lower(),
                                                Approaches=row[26].lower(),
                                                Indifferent=row[27].lower(),
                                                RunsFrom=row[28].lower(),
                                                )
                                    added_sightings.save()
                except:
                    return "Sorry, something went wrong"
