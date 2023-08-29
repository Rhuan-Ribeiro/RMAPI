from django.contrib import admin
from .models import *

# Register your models here.

class detCharacter(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'species')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Character, detCharacter)

class detLocation(admin.ModelAdmin):
    list_display = ('id', 'name', 'locationType')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Location, detLocation)

class detEpisode(admin.ModelAdmin):
    list_display = ('id', 'name', 'episode', 'air_date')
    list_display_links = ('id', 'name', 'episode',)
    search_fields = ('name', 'episode',)
    list_per_page = 10

class detCharacter_Episode(admin.ModelAdmin):
    list_display = ('id', 'character_fk', 'episode_fk')
    list_display_links = ('id')
    search_fields = ('id', 'name', 'episode',)
    list_per_page = 10

admin.site.register(Episode, detEpisode)
