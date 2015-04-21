from rottentomatoes import RT
import logging
import os
import django
from django.shortcuts import get_object_or_404
logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviewhereabouts.settings")

django.setup()

from asteroid.models import Movie, Cast

my_key = '662g9gvhs6kcgwyj5aqn5j25'

latest = RT(my_key).lists('movies', 'in_theaters', page=1)

p = get_object_or_404(Cast, movie=1)
print "Getting latest movies..."

try:
    print "Connecting to rottentomatoes.com ..."
    c = models.Cast(actor = "actors", character = "characters")
    c.save()
    print "Successfully added"+"Alaska finally!"

except:
    logger.debug("Unsuccessful:"+str(c))
    print "could not save:"+"Alaska"

