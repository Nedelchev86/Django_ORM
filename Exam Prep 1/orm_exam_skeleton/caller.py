import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# Create and run your queries within functions
from django.db.models import Q
from main_app.models import Director

def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""
    directors = ""
    if search_name is not None and search_nationality is not None:
        directors = Director.objects.filter(full_name__icontains=search_name, nationality__icontains=search_nationality).order_by("full_name")
    elif search_name is not None:
        directors = Director.objects.filter(full_name__icontains=search_name).order_by("full_name")
    elif search_nationality is not None:
        directors = Director.objects.filter(nationality__icontains=search_nationality).order_by("full_name")

    if not directors:
        return ""

    return "\n".join([f"Director: {director.full_name}, nationality: {director.nationality}, experience: {director.years_of_experience}" for director in directors])


    # query = Q()
    # query_name = Q(full_name__icontains=search_name)
    # query_nationality = Q(nationality__icontains=search_nationality)
    #
    # if search_name is not None and search_nationality is not None:
    #     query |= query_name & query_nationality
    # elif search_name is not None:
    #     query |= query_name
    # else:
    #     query |= query_nationality
    #
    # directors = Director.objects.filter(query).order_by('full_name')
    #
    # if not directors:
    #     return ""
    #
    # return "\n".join([f"Director: {director.full_name}, nationality: {director.nationality}, experience: {director.years_of_experience}" for director in directors])
    #
    #
    #

def get_top_director():
    director = Director.objects.get_directors_by_movies_count().first()
    if not director:
        return ""
    return f"Top Director: {director.full_name}, movies: {director.movies.count()}."