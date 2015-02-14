#!/usr/bin/env python
import simplejson
import requests
import os
import django
import logging
import math

logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviewhereabouts.settings")

django.setup()

from asteroid import models

key = "662g9gvhs6kcgwyj5aqn5j25"
url = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey=%s"
res = requests.get(url % key)
data = res.content
js = simplejson.loads(data)
movies = js["movies"]

print "Getting latest movies..."

for movie in movies:
    actors = ""
    characs = ""
    for actor in movie["abridged_cast"]:
        actors = actor["name"] + ","

    for actor in movie["abridged_cast"]:
        characs = actor["characters"][0] + ","

    m = models.Movie(title = movie["title"], movie_synopsis = movie["synopsis"], critics_score = movie["ratings"]["critics_score"], release = movie["year"], actor = actors, character = characs)

    try:
        m.save()
    except:
        logger.debug("Could not save:"+str(m))
        print "could not save.."

    print "Successfully updated:", movie["title"]



