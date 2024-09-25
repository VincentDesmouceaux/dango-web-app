# ~/projects/django-web-app/merchex/listings/views.py

from listings.models import Band
from django.http import HttpResponse
from django.shortcuts import render
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect  # ajoutez cet import
from listings.forms import BandForm, ContactUsForm


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


def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {
                    form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
        return redirect('contact')  # ajoutez cette instruction de retour

    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
                  'listings/contact.html',
                  {'form': form})


# listings/views.py

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            return redirect('band-detail', band.id)
    else:
        # Si c'est une requête GET ou si le formulaire n'est pas valide
        form = BandForm()

    # Toujours retourner un HttpResponse
    return render(request, 'listings/band_create.html', {'form': form})


def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            # Correction: suppression de la parenthèse en trop
            return redirect('band-detail', band.id)
    else:
        # Si c'est une requête GET ou si le formulaire n'est pas valide
        form = BandForm(instance=band)

    # Toujours retourner un HttpResponse
    return render(request, 'listings/band_update.html', {'form': form})
