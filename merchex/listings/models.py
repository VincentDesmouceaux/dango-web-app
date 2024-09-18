# listings/models.py

from django.db import models

# Create your models here.


# listings/models.py

from django.core.validators import MaxValueValidator, MinValueValidator
...


class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)

    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Listing(models.Model):

    class ListingType(models.TextChoices):
        RECORDS = 'R'
        CLOTHING = 'C'
        POSTERS = 'P'
        MISC = 'M'

    # Nom de l'élément de la liste
    name = models.fields.CharField(max_length=100)
    type = models.fields.CharField(choices=ListingType.choices, max_length=5)
    description = models.fields.CharField(max_length=1000)
    year = models.fields.IntegerField(
        null=True,
        validators=[MinValueValidator(1900),
                    MaxValueValidator(2021)]
    )
    sold = models.fields.BooleanField(default=False)

    # Ajout du champ ForeignKey pour lier à un Band
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class ListingType(models.TextChoices):
        RECORDS = 'R'
        CLOTHING = 'C'
        POSTERS = 'P'
        MISC = 'M'

    # Changement de title à name pour cohérence
    name = models.fields.CharField(max_length=100)
    type = models.fields.CharField(choices=ListingType.choices, max_length=5)
    description = models.fields.CharField(max_length=1000)
    year = models.fields.IntegerField(
        null=True,
        validators=[MinValueValidator(1900),
                    MaxValueValidator(2021)]
    )
    sold = models.fields.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'
