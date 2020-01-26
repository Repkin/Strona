from django.forms import ModelForm
from .models import Movie

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'year', 'released', 'imbd_rating']