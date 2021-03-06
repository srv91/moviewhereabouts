from django.contrib import admin
from asteroid.models import Movie, Cast, Feedback

class CastInLine(admin.StackedInline):
    model = Cast

class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['id']}),
        (None, {'fields': ['imdb_id']}),
        (None, {'fields': ['tmdb_id']}),
        (None, {'fields': ['title']}),
        (None, {'fields': ['movie_synopsis']}),
        (None, {'fields': ['critics_score']}),
        (None, {'fields': ['genre']}),
        (None, {'fields': ['s_img']}),
        (None, {'fields': ['votes']}),
    ]
    inlines = [CastInLine]
    list_display = ('title', 'genre')

class CastAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Major cast', {'fields': ['actor', 'character']}),
    ]
    list_display = ('movie', 'actor')

class FeedbackAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['fname']}),
        (None, {'fields': ['fmail']}),
        (None, {'fields': ['msg']}),
    ]
    list_display = ('fname', 'fmail')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Cast, CastAdmin)
admin.site.register(Feedback, FeedbackAdmin)


