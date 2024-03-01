from django.urls import path, include

from . import views

app_name='user_reg'

urlpatterns = [
    path('register', views.register,name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # path('profile/<username_id>', views.profile, name='profile'),
    # path('edit_profile/<username_id>', views.edit_profile, name='edit_profile'),


]