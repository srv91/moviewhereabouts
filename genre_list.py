import logging
import os
import django

logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviewhereabouts.settings")

django.setup()

from asteroid import models
from asteroid.models import Movie
genres = []
for movie in Movie.objects.all():
    g = movie.genre
    for g1 in g.split(', '):
        if g1 not in genres:
            genres.append(g1)

print genres
print len(genres)
