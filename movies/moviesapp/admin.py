from django.contrib import admin

# Register your models here.

from .models import Category, Genre, Actor, Movie, MovieShots, Rating, RatingStar, Reviews

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)

