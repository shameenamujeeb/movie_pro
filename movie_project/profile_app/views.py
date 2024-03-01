from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.template import context

from movies_app.forms import MovieForm
from movies_app.models import Movie
from profile_app.forms import ProfileForm
from profile_app.models import Profile


# vie profile page
def profile(request):
    usr1 = request.user
    movie_list = Movie.objects.all().filter(username=usr1)
    return render(request, 'profile.html', {'user': usr1, 'mov': movie_list})


# edit profile page
def edit_profile(request, username_id):
    profile = User.objects.get(id=username_id)
    frm = ProfileForm()
    if request.POST:
        print(profile)
        frm = ProfileForm(request.POST or None, request.FILES, instance=profile)

        if frm.is_valid():
            frm.save()
            profile.save()
            p = Profile(username_id=username_id)
            p.save();
            messages.info(request, "success")
            messages.success(request, 'your profile updated')
            return redirect('profile_app:profile')
    return render(request, 'edit_profile.html', {'profile': profile, 'frm': frm})


# Deletion of amovie
def delete_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)

    movie.delete()
    print("success")
    return redirect('profile_app:profile')


#  update movie

def update_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    frm = ProfileForm()
    if request.POST:
        print(profile)
        frm = MovieForm(request.POST or None, request.FILES, instance=movie)
        if frm.is_valid():
            frm.save()
            messages.info(request, "success")
    return render(request, 'edit_movie.html', {'movie_detail': movie, 'frm': frm})


# edit movies

def edit_mov(request, movie_id):
    url = request.META.get('HTTP_REFERER')
    user = request.user.id
    desc = Movie.objects.get(id=movie_id, username_id=user)
    frm = MovieForm()
    if request.POST:
        frm = MovieForm(request.POST or None, request.FILES, instance=desc)
        if frm.is_valid():
            frm.save()
        # messages.success(request, "movie f'{{desc.title}}' updated successfully")
            return redirect(url)

    return render(request, "edit_movie.html", {'mov_detail': desc, 'frm': frm})
