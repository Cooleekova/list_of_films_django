from django.contrib import admin

# Register your models here.

from films.models import Film


@admin.register(Film)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'length', 'title', 'subject', 'actor', 'actress', 'director', 'popularity')
