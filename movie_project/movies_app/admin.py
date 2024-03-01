from django.contrib import admin

from .models import Category, Movie, ReviewRating


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'slug']

    list_per_page = 20


class RateAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'review', 'rating', 'created_date']
    list_per_page = 20


admin.site.register(ReviewRating, RateAdmin)

admin.site.register(Movie, MovieAdmin)
