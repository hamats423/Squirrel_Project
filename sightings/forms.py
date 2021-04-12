from django.forms import ModelForm
from .models import Sightings

class SightingsForm(ModelForm):
    class Meta:
        model = Sightings
        fields = '__all__'
        help_texts = {'Date':('When did you sight the squirrel? (YYYY-MM-DD)')}

