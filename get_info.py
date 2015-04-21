from rottentomatoes import RT
import logging
import os
import django

logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviewhereabouts.settings")

django.setup()

from asteroid import models
from asteroid.models import Movie
import time
my_key = '662g9gvhs6kcgwyj5aqn5j25'
for movie in Movie.objects.all():
    print movie.id
    print movie.title
    mov = RT(my_key).info(movie.id)

    try:
        m = models.Movie(id = mov['id'], imdb_id = mov['alternate_ids']['imdb'], title = mov['title'], movie_synopsis = mov['synopsis'], critics_score = mov['ratings']['critics_score'], release = mov['year'], votes = 10, img = mov['title'].replace(" ","").lower(), category = 'latest')
        m.save()
    except:
        print "could not save: "+mov['title']

    print "updated:"+mov['title']

print "update complete!"

