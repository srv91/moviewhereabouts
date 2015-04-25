import os
import django
import logging

logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviewhereabouts.settings")

django.setup()

from asteroid import models
from asteroid.models import Movie
my_key = 'fc86d622a7b420430bdc23693434dded'

import urllib
from urllib2 import urlopen
import requests
import time
import json

for movie in Movie.objects.all():
    imdbid = movie.imdb_id
    print imdbid
    imdbid = ''.join(('tt',imdbid))

    try:
        link = "http://api.themoviedb.org/3/movie/"
        url = "%s%s?api_key=%s"
        url = url % (link, imdbid, my_key)
        res = urlopen(url).read()
        js = json.loads(res)
        print movie.title
        print js['id']
        genre_list = []
        for g in js['genres']:
            genre_list.append(g['name'])
        found_genre = ''.join(genre_list)
        print found_genre
        m = models.Movie(id = movie.id, imdb_id = movie.imdb_id, tmdb_id = movie.tmdb_id, title = movie.title, movie_synopsis = movie.synopsis, critics_score = movie.critics_score, votes = 10, img = movie.img, category = 'latest', genre = found_genre)
        m.save()
        print "genre updated!"
        print "updated:"+movie.title
    except:
        print "could not save:"+movie.title
print "Update complete!"

