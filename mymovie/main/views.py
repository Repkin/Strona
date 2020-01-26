from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie
from .forms import MovieForm
# Create your views here.

def wszystkie_filmy(request):
    text_views = "WSB"
    # filmy = ["Władca Pierścieni","Harry Potter","Killer"]
    filmy = Movie.objects.all()
    moze_ogladac = True
    return render(request,'lista_filmow.html',
                  {'text':text_views,"filmy":filmy,"moze_ogladac":moze_ogladac})

def nowy_film(request):
    form = MovieForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)

    return render(request,'film_form.html',{'form':form})


def edytuj_film(request, id):
    film = get_object_or_404(Movie,pk=id)
    form = MovieForm(request.POST or None,instance=film)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form})


def usun_film(request, id):
    film = get_object_or_404(Movie,pk=id)

    if request.method == 'POST':
        film.delete()
        return  redirect(wszystkie_filmy)

    return render(request, 'potwierdz.html',{'film':film})