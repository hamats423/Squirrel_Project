from django.db import models
from django.urls import reverse

class Sighting(models.Model):
    Latitude=models.FloatField(    
            help_text=('Sighting Latitude: '),
    	    blank=True,
            )
    
    Longitude=models.FloatField(
            help_text=('Sighting Longitude'),
            blank=True,
            )
    
    UniqueSquirrelID=models.CharField(
            max_length=100,
            help_text=('Squirrel ID'),
            blank=True,
            )
    
    AM,PM='AM','PM'

    Shift_Choices=(
            (AM,'AM'),
            (PM,'PM'),
            )

    Shift=models.CharField(
            max_length=2,
            choices=Shift_Choices,
            help_text=('Sighting Shift'),
            blank=True,
            )
    
    Date=models.DateField(
            help_text=('Sighting Date'),
            blank=True,
            )

    ADULT, JUVENILE = 'Adult', 'Juvenile'

    Age_Choices=(
            (ADULT, 'Adult'),
            (JUVENILE, 'Juvenile'),
            )

    Age=models.CharField(
            max_length=20,
            choices=Age_Choices,
            help_text=("Squirrel's age"),
            blank=True,
            )

    BLACK, GRAY, CINNAMON = 'Black', 'Gray', 'Cinnamon'

    Primary_Fur_Color_Choices = (
            (BLACK,'Black'),
            (GRAY,'Gray'),
            (CINNAMON,'Cinnamon'),
            )

    Primary_Fur_Color=models.CharField(
            max_length=20,
            choices = Primary_Fur_Color_Choices,
            help_text=('Primary Fur Color'),
            blank=True,
            )

    ABOVEGROUND, GROUNDPLANE = 'Above Ground', 'Ground Plane'

    Location_Choices=(
            (ABOVEGROUND, 'Above Ground'),
            (GROUNDPLANE, 'Ground Plane'),
            )

    Location=models.CharField(
            max_length = 20,
            choices=Location_Choices,
            help_text=('Sighting Location'),
            blank=True,
            )

    SpecificLocation=models.CharField(
            max_length=100,
            help_text=('Sighting Specific Location'),
            blank=True,
            )

    OtherActivities=models.CharField(
            max_length=100,
            help_text=('Other Activities'),
            blank=True,
            )

    true,false='true','false'

    bool_choices=(
            (true,'true'),
            (false,'false'),
            )

    Running=models.CharField(
            max_length=20,
            choices=bool_choices,
            help_text=('Is the squirrel running?'),
            blank=True,
            )

    Chasing=models.CharField(
            max_length=20,
            choices=bool_choices,
            help_text=('Is the squirrel chasing another squirrel?'),
            blank=True,
            )

    Climbing=models.CharField(
            max_length=5,
            choices=bool_choices,
            help_text=('Is the squirrel climbing?'),
            blank=True,
            )

    Eating=models.CharField(
            max_length=5,
            choices=bool_choices,
            help_text=('Is the squirrel eating?'),
            blank=True,
            )

    Foraging=models.CharField(
            max_length=5,
            choices=bool_choices,
            help_text=('Is the squirrel foraging?'),
            blank=True,
            )

    Kuks=models.CharField(
            max_length=5,
            choices=bool_choices,
            help_text=('Did the squirrel kuk?'),
            blank=True,
            )

    Quaas=models.CharField(
            max_length=5,
            choices=bool_choices,
            help_text=('Did the squirrel quaa?'),
            blank=True,
            )

    Moans=models.CharField(
            max_length=5,
            choices=bool_choices,
            help_text=('Did the squirrel moan?'),
            blank=True,
            )

    TailFlags=models.CharField(
            max_length=5,
            choices=bool_choices,
            help_text=('Did its tail flag?'),
            blank=True,
            )

    TailTwitches=models.CharField(
            max_length=5,
            choices=bool_choices,
            help_text=('Did its tail twitch?'),
            blank=True,
            )

    Approaches=models.CharField(
            max_length=5,
            choices=bool_choices,
            help_text=('Did it approach you?'),
            blank=True,
            )

    Indifferent=models.CharField(
            max_length=5,
            choices=bool_choices,
            help_text=('Was it indifferent towards you?'),
            blank=True,
            )

    RunsFrom=models.CharField(
            max_length=5,
            choices=bool_choices,
            help_text=('Did it run from you?'),
            blank=True,
            )

    def __str__(self):
        return self.UniqueSquirrelID

    def get_absolute_url(self):
        return reverse('index')




