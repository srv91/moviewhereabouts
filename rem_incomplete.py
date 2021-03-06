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
    if movie.movie_synopsis:
        print "skip movie:"+movie.title
    else:
        imdbid = movie.imdb_id
        if imdbid:
            print imdbid
            imdbid = ''.join(('tt',imdbid))
        elif imdbid == 0:
            movie.delete()
            break;
        try:
            link = "http://api.themoviedb.org/3/movie/"
            url = "%s%s?api_key=%s"
            url = url % (link, imdbid, my_key)
            res = urlopen(url).read()
            js = json.loads(res)
            syno = js['overview']
            if syno:
                movie.movie_synopsis = syno
                movie.save()
            else:
                movie.delete()
        except:
            print "action incomplete!"
print "successfull!"
