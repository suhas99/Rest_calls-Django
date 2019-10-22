from django.contrib import admin
from .models import personDetails


class personDetailsAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'email', 'github')


admin.site.register(personDetails, personDetailsAdmin)
