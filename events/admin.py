from django.contrib import admin
from .models import Venue

# Method 1


# class VenueAdmin(admin.ModelAdmin):
#     list_display = ('capacity', 'name', 'address')

# admin.site.register(Venue, VenueAdmin)


# Method 2

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'capacity', 'address')
    list_display_links = ('capacity',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_editable = ('name', 'address')
