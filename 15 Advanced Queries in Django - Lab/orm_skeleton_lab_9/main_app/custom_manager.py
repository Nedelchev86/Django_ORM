from django.db import models




class ProductManager(models.Manager):

    def available_products(self):
        return self.filter(is_available=True)