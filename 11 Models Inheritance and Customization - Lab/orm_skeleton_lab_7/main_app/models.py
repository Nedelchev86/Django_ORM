from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


def validate_specialities(value):
    if value not in ["Mammals", "Birds", "Reptiles", "Others"]:
        raise ValidationError("Specialty must be a valid choice.")


class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    sound = models.CharField(max_length=100)


class Mammal(Animal):
    fur_color = models.CharField(max_length=50)


class Bird(Animal):
    wing_span = models.DecimalField(max_digits=5, decimal_places=2)


class Reptile(Animal):
    scale_type = models.CharField(max_length=50)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

    class Meta:
        abstract=True


SPECIALITIES = (
    ("Mammals", "Mammals"),
    ("Birds", "Birds"),
    ("Reptiles", "Reptiles"),
    ("Others", "Others")
)


class ZooKeeper(Employee):
    specialty = models.CharField(max_length=10, choices=SPECIALITIES)
    managed_animals = models.ManyToManyField("Animal")

    def clean(self):
        super().clean()

        if self.specialty not in ["Mammals", "Birds", "Reptiles", "Others"]:
            raise ValidationError("Specialty must be a valid choice.")



class Veterinarian (Employee):
    license_number = models.CharField(max_length=10)


class ZooDisplayAnimal(Animal):

    def extra_info(self):
        result = ""
        if hasattr(self, "mammal"):
            result = f"Its fur color is {self.mammal.fur_color}."
        elif hasattr(self, "bird"):
            result = f"Its wingspan is {self.bird.wing_span} cm."
        elif hasattr(self, "reptile"):
            result = f"Its scale type is {self.reptile.scale_type}."
        return result

    def display_info(self):
        return f"Meet {self.name}! It's {self.species} and it's born {self.birth_date}. It makes a noise like '{self.sound}'!{self.extra_info()}"

    def is_endangered(self):
        return self.species in ["Cross River Gorilla", "Orangutan", "Green Turtle"]

    class Meta:
        proxy = True


