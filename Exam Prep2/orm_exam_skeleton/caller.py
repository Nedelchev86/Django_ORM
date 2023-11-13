import os
import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Product

# Create and run your queries within functions

# profile1 = Profile(full_name="Tihomir Nedelchev", email="soyo@abv.bg", phone_number="08998889333", address="Bourgas")
# profile2 = Profile(full_name="Tihomir ", email="soyo@ab.bg", phone_number="08998889332", address="Varna")
# profile3 = Profile(full_name="Nedelchev", email="soyo@a.bg", phone_number="08998889331", address="Ruse")
#
# profile1.save()
# profile2.save()
# profile3.save()

# product1 = Product(name="Laptop", description="Assus", price="100.20", in_stock="3")
# product2 = Product(name="Laptop2", description="Acer", price="200.20", in_stock="2")
# product3 = Product(name="Laptop3", description="Lenovo", price="300.20", in_stock="5")

# product1.save()
# product2.save()
# product3.save()



# print(Profile.objects.get_regular_customers())