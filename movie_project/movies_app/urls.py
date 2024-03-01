from django.urls import path
from django.contrib import admin
from .import views
app_name="movies_app"
urlpatterns = [

    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.movie_detail,name='movie_detail' ),
    path('<slug:home_slug>/', views.index, name='movie_by_category'),
    # path('<slug:home_slug>/', views.index, name='movie_by_language'),
    path('add_movie/<int:username_id>/',views.add_movie,name='add_movie'),
    path('movie/<int:movie_id>/add_review/',views.add_review,name='add_review'),
    path('movie/<int:movie_id>/<int:rev_id>',views.delete_review,name='delete_review'),




    ]