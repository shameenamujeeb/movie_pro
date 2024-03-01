from django.db.models import Q
from django.shortcuts import render

from movies_app.models import Movie


def SearchResult(request):
    movie=None
    query= None
    if 'q' in request.GET:
        query=request.GET.get('q')
        movie=Movie.objects.all().filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(language__icontains=query))
        print(movie)

        print(query)
    return render(request,'search.html',{'query':query,'moves':movie})