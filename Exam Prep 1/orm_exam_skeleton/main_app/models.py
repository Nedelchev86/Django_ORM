from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.


class Director(models.Model):
    full_name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])
    birth_date = models.DateField(default="1900-01-01")
    nationality = models.CharField(max_length=50, default="Unknown")
    years_of_experience = models.SmallIntegerField(MinValueValidator(0), default="0")


class Actor(models.Model):
    full_name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])
    birth_date = models.DateField(default="1900-01-01")
    nationality = models.CharField(max_length=50, default="Unknown")
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)


MOVIES = (
    ('Action','Action'),
    ('Comedy','Comedy'),
    ('Drama', 'Drama'),
    ('Other', 'Other')
)


class Movie(models.Model):
    title = models.CharField(max_length=150, validators=[MinLengthValidator(5)])
    release_date = models.DateField()
    storyline = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=6, choices=MOVIES, default="Other")
    rating = models.DecimalField(
        max_digits=3, decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        default="0.0")
    is_classic = models.BooleanField(default=False)
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
    director = models.ForeignKey(to="Director", on_delete=models.CASCADE)
    starring_actor = models.ForeignKey(to="Actor", on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField(to="Actor")
