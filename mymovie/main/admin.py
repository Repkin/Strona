from django.contrib import admin
from .models import Movie
# Register your models here.

# admin.site.register(Movie)



@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ("name", 'description', "year", "released", "imbd_rating")
    list_display = ("name", 'description', "year", "released", "imbd_rating")
    list_filter=("year", "released")
    search_fields = ("name","description")