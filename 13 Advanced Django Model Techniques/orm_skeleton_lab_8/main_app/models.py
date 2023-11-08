from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2, "Name must be at least 2 characters long."),
                    MaxLengthValidator(100, "Name cannot exceed 100 characters.")]
    )
    location = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Location must be at least 2 characters long."),
                                            MaxLengthValidator(200, "Location cannot exceed 200 characters.")])

    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0, "Rating must be at least 0.00."),
                    MaxValueValidator(5, "Rating cannot exceed 5.00.")])
