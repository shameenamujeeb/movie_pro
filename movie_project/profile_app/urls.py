from django.urls import path
from django.contrib import admin
from .import views
app_name="profile_app"
urlpatterns = [


    path('profile', views.profile, name='profile'),
    path('edit_profile/<username_id>', views.edit_profile, name='edit_profile'),
    path('edit_mov/<movie_id>',views.edit_mov,name='edit_mov'),
    path('delete_movie/<movie_id>', views.delete_movie, name='delete_movie'),
    path('update_movie/<movie_id>', views.update_movie, name='update_movie'),



    ]