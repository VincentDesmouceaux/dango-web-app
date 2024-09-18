# ~/projects/django-web-app/merchex/listings/views.py

from listings.models import Band
from django.http import HttpResponse
from django.shortcuts import render
# listings/views.py


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html',
                  {'bands': bands})


def band_list(request):
    # Récupère tous les objets Band
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


def band_detail(request, id):
    # nous insérons cette ligne pour obtenir le Band avec cet id
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  # nous mettons à jour cette ligne pour passer le groupe au gabarit
                  {'band': band})


def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')
