import logging
import os
import django

logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviewhereabouts.settings")

django.setup()

from asteroid import models
from asteroid.models import Movie

for movie in Movie.objects.all():
    try:
        image = movie.img
        simage = ''.join(('http://image.tmdb.org/t/p/w185', image))
        limage = ''.join(('http://image.tmdb.org/t/p/w342', image))
        movie.s_img = simage
        movie.l_img = limage
        movie.save()
        print "updated:"+movie.title
    except:
        print "could not update:"+movie.title
print "Update complete!"
