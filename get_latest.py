from rottentomatoes import RT
import logging
import os
import django

logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviewhereabouts.settings")

django.setup()

from asteroid import models

my_key = '662g9gvhs6kcgwyj5aqn5j25'

latest = RT(my_key).lists('movies', 'in_theaters', page=1)

print "Getting latest movies..."

for movie in latest['movies']:
    for actor in movie['abridged_cast']:
        actors = actor['name'] + ","
    actors[:-1]

    for actor in movie['abridged_cast']:
        characs = actor['characters'][0] + ","
    characs[:-1]

    m = models.Movie(title = movie['title'], movie_synopsis = movie['synopsis'], critics_score = movie['ratings']['critics_score'], release = movie["year"], actor = actors, character = characs)

    try:
        m.save()
    except:
        logger.debug("Could not save:"+str(m))
        print "could not save.."

    print "Successfully updated:", movie['title']

