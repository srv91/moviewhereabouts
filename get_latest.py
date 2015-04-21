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

try:
    print "Connecting to rottentomatoes.com ..."
    for movie in latest['movies']:
        #mid = movie['id']

        #for movie_id in models.Movie:
            #if mid = movie_id:
                #print movie['title']+"already exists."
                #break;


        actors = ""
        characs = ""
        for actor in movie['abridged_cast']:
            actors += actor['name']+","
            characs += actor['characters'][0]+","
        characs[:-1]
        actors[:-1]

        m = models.Movie(id = movie['id'], title = movie['title'], movie_synopsis = movie['synopsis'], critics_score = movie['ratings']['critics_score'], release = movie['year'], votes = 10)
        c = models.Cast(actor = "actors", character = "characters")
        m.save()
        c.save()

except:
    logger.debug("Unsuccessful:"+str(m))
    print "could not save:"+movie['title']

print "Successfully updated!"
