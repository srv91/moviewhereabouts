from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 40)
    user_fav = models.CommaSeparatedIntegerField(max_length = 50)

    def __str__(self):
        return self.username

class Movie(models.Model):
    id = models.IntegerField(default = 0, primary_key=True)
    imdb_id = models.CharField(max_length = 25, default = '')
    tmdb_id = models.CharField(max_length = 25, default = '')
    title = models.CharField(max_length = 100)
    movie_synopsis = models.CharField(max_length = 1800)
    critics_score = models.IntegerField(default = 0)
    votes = models.IntegerField(default = 10)
    img = models.CharField(max_length = 50, default = 'Image unavailable')
    s_img = models.CharField(max_length = 70, default = '')
    l_img = models.CharField(max_length = 70, default = '')
    category = models.CharField(max_length = 20)
    genre = models.CharField(max_length = 60)

    def __str__(self):
        return self.title

class Cast(models.Model):
    movie = models.ForeignKey(Movie, unique=True)
    actor = models.CharField(max_length = 200)
    character = models.CharField(max_length = 200)

    def __str__(self):
        return self.movie.title

class Feedback(models.Model):
    fname = models.CharField(max_length = 25, default='unknown')
    fmail = models.EmailField(max_length = 50, default='unknown@unknown.com')
    msg = models.CharField(max_length = 200, default='no msg')

    def __str__(self):
        return self.fname


