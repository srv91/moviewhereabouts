from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from asteroid.models import Movie, Cast, Feedback
import urllib
from urllib2 import urlopen
import requests
import json
from rottentomatoes import RT
from django.db import connection
from urllib import urlencode
import zlib
from django.core.validators import validate_email

def browse(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 9)
    page = request.GET.get('page')

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    return render(request, 'asteroid/browse.html', {'movies': movies})

def browse_genre(request, g):
    if g:
        for movie in Movie.objects.all():
            found_movies = Movie.objects.filter(genre__icontains=g)
    else:
        found_movies = Movie.objects.all()
    paginator = Paginator(found_movies, 9)
    page = request.GET.get('page')

    try:
        found_movies = paginator.page(page)
    except PageNotAnInteger:
        found_movies = paginator.page(1)
    except EmptyPage:
        found_movies = paginator.page(paginator.num_pages)

    return render(request, 'asteroid/browse-genre.html', {'movies': found_movies})

def index(request):
    latest_movies = Movie.objects.all()
    context = {'latest_movies': latest_movies}
    return render(request, 'asteroid/index.html', context)

def indextop(request):
    top_movies = Movie.objects.order_by('-votes')
    context = {'top_movies': top_movies}
    return render(request, 'asteroid/indextop.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'asteroid/detail.html', {'movie': movie})

def voting(request, movie_id):
    try:
        m = get_object_or_404(Movie, pk=movie_id)
        #p = get_object_or_404(Vote, movie=movie_id)
        m.votes += 1
        m.save()
    except (KeyError):
        # Redisplay the movie voting form.
        return render(request, 'asteroid/detail.html', {
            'movie': m,
            'error_message': "Error:Please vote again.",
        })

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('asteroid:detail', args=(m.id,)))

def welcome(request):
    latest_movies = Movie.objects.filter(category='latest')[:3]
    top_movies = Movie.objects.order_by('-votes')[:3]
    context = {'latest_movies': latest_movies, 'top_movies': top_movies}
    return render(request, 'asteroid/welcome.html', context)

def screen1(request):
    return render(request, 'asteroid/screen1.html')

def search(request):
    if 'q' in request.POST and request.POST['q']:
        q = request.POST['q']
        found_movies = Movie.objects.filter(title__icontains=q)
        if found_movies:
            context = {'movies': found_movies}
            return render(request, 'asteroid/search.html', context)
        else:
            my_key = '662g9gvhs6kcgwyj5aqn5j25'
            tmdb_key = 'fc86d622a7b420430bdc23693434dded'
            found = RT(my_key).search(q, page_limit=4)
            for movie in found:
                try:
                    rt_id = movie['id']
                    o_imdbid = movie['alternate_ids']['imdb']
                    imdbid = ''.join(("tt",o_imdbid))
                    link = "http://api.themoviedb.org/3/movie/"
                    url = "%s%s?api_key=%s"
                    url = url % (link, imdbid, tmdb_key)
                    res = urlopen(url).read()
                    js = json.loads(res)
                    tmdbid = js['id']
                    genre_list = []
                    for g in js['genres']:
                        genre_list.append(g['name'])
                    found_genre = ', '.join(genre_list)
                    print movie['title']
                    image = js['poster_path']
                    simage = ''.join(('http://image.tmdb.org/t/p/w185', image))
                    limage = ''.join(('http://image.tmdb.org/t/p/w342', image))
                    if movie['synopsis']:
                        syno = movie['synopsis']
                    else:
                        syno = js['overview']
                    m = Movie(id = rt_id, imdb_id = o_imdbid, tmdb_id = tmdbid, title = movie['title'], movie_synopsis = syno, critics_score = movie['ratings']['critics_score'], votes = 10, img = image, s_img = simage, l_img = limage, genre = found_genre)
                    m.save()
                    m.update()
                except:
                    print "could not save: "+movie['title']
                    break;
            found_movies = Movie.objects.filter(title__icontains=q)
            context = {'movies': found_movies}
            return render(request, 'asteroid/search.html', context)
    else:
        found_movies = 0
        context = {'movies': found_movies}
        return render(request, 'asteroid/search.html', context)

def about(request):
    context = {'tags': False, 'success': True, 'valid': True}
    return render(request, 'asteroid/about.html', context)

def feedback(request):
    if 'name' in request.POST and request.POST['name']:
        if 'email' in request.POST and request.POST['email']:
            if 'message' in request.POST and request.POST['message']:
                name = request.POST['name']
                email = request.POST['email']
                message = request.POST['message']

            try:
                validate_email(email)
                valid = True
            except ValidationError:
                valid = False

            f = Feedback(fname = str(name), fmail = email, msg = str(message))
            f.save()
            context = {'tags': True, 'success': True, 'valid': valid}
            return render(request, 'asteroid/about.html', context)
    else:
        context = {'tags': True, 'success': False, 'valid': True}
        return render(request, 'asteroid/about.html', context)


