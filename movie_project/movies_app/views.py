from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .forms import MovieForm, ReviewForm
from .models import Movie, Category, ReviewRating


# Create your views here.
# home page
def index(request, home_slug=None):
    home_page = None
    movie_list = None
    if (home_slug != None):
        home_page = get_object_or_404(Category, slug=home_slug)
        movie_list = Movie.objects.all().filter(genere=home_page)
    else:
        movie_list = Movie.objects.all()
    paginator = Paginator(movie_list, 8)
    try:
        page = request.GET.get('page', '1')
    except:
        page = 1
    try:
        mov = paginator.page(page)
    except (EmptyPage, InvalidPage):
        mov = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'category': home_page, 'movielist': mov})

# movie Details
def movie_detail(request, movie_id):
    desc = Movie.objects.get(id=movie_id)
    revi = ReviewRating.objects.filter(title=desc)
    user = request.user.id

    return render(request, "detail.html", {'mov_detail': desc, 'review': revi})

# Add movies
def add_movie(request, username_id):
    prof = User.objects.get(id=username_id)
    frm = MovieForm()
    if request.POST:
        frm = MovieForm(request.POST or None, request.FILES)
        if frm.is_valid():
            r = frm.save()
            r.username_id = prof
            r.save()
            return redirect('profile_app:profile')
        else:
            frm = MovieForm
    return render(request, 'add.html', {'frm': frm})

#  Review add
def add_review(request, movie_id):
    url = request.META.get('HTTP_REFERER')
    movie = Movie.objects.get(id=movie_id)
    form = ReviewForm(instance=movie)
    if request.POST:
        form = ReviewForm(request.POST, instance=movie)
        if form.is_valid():
            name = request.user.username
            body = request.POST['review']
            rate = form.cleaned_data['rating']
            rev = ReviewRating(title=movie, username=name, review=body, rating=rate)
            rev.save()
            messages.info(request, "Thank you! Your review has beem submitted.")
            return redirect(url)
        else:
            form = ReviewForm()

            return redirect(url)
    return render(request, "detail.html", {'form': form, 'movie': movie})

# review delete
def delete_review(request, movie_id,rev_id):
    url = request.META.get('HTTP_REFERER')
    user = request.user.username
    reviw = ReviewRating.objects.all().filter(title_id=movie_id, username=user,id=rev_id)
    reviw.delete()
    # messages.info(request,"your review deleted successfully")
    return redirect(url)
