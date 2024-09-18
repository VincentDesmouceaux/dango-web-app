from django.contrib import admin
from .models import Band, Listing


class ListingAdmin(admin.ModelAdmin):
    # Remplacer 'title' par 'name' pour correspondre au modèle Listing
    list_display = ('name', 'band', 'type', 'year', 'sold')


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')


admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
