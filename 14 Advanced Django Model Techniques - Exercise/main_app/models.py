from django.core.validators import MinValueValidator
from django.db import models

from main_app.validators import name_validator, phone_validator


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100, validators=[name_validator])
    age = models.PositiveIntegerField(validators=[MinValueValidator(18, "Age must be greater than 18")])
    email = models.EmailField(error_messages={"invalid": "Enter a valid email address"})
    phone_number = models.CharField(max_length=13, validators=[phone_validator])
    website_url = models.URLField(error_messages={"invalid": "Enter a valid URL"})