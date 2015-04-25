import logging
import os
import django

logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviewhereabouts.settings")

django.setup()

from asteroid import models
from asteroid.models import Movie

for movie in Movie.objects.all():
    r = movie.imdb_id
    print r
    if r == 0:
        movie.delete()
    else:
        movie.release = int(r)
        movie.save()
