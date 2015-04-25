from rottentomatoes import RT
import logging
import os
import django

logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviewhereabouts.settings")

django.setup()

from asteroid import models
from asteroid.models import Movie
my_key = '662g9gvhs6kcgwyj5aqn5j25'

latest = RT(my_key).lists('movies', 'opening')

print "Getting latest movies..."
for movie in latest['movies']:
    if Movie.objects.filter(id = movie['id']).exists()==False:
        try:
            m = models.Movie(id = movie['id'], imdb_id = movie['alternate_ids']['imdb'], title = movie['title'], movie_synopsis = movie['synopsis'], critics_score = movie['ratings']['critics_score'], votes = 10, img = movie['title'].replace(" ","").lower(), category = 'latest')
            m.save()

        except:
            logger.debug("Unsuccessful:"+str(m))
            print "could not save: "+movie['title']
            break;

        print "updated:"+movie['title']

print "Update complete!"
