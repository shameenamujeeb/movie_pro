from django.contrib import admin

from .models import Profile, Movie, ProfileItems


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'created', 'updated']

    list_per_page = 20


class ProfileItemsAdmin(admin.ModelAdmin):
    list_display = ['username', 'movie_name', 'profile', 'created']
    list_per_page = 20
admin.site.register(Profile, ProfileAdmin)

admin.site.register(ProfileItems, ProfileItemsAdmin)
