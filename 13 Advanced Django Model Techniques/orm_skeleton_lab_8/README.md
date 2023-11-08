
1.	Restaurant
In the main_app create a model called "Restaurant" with the following fields:
•	name
o	A character field.
o	Validations:
	Minimum length of 2 characters with a custom error message "Name must be at least 2 characters long."
	Maximum length of 100 characters with a custom error message "Name cannot exceed 100 characters."
o	Represents the name of the restaurant.
•	location
o	A character field.
o	Validations:
	Minimum length of 2 characters with a custom error message "Location must be at least 2 characters long."
	Maximum length of 200 characters with a custom error message "Location cannot exceed 200 characters."
o	Represents the location of the restaurant.
•	description
o	A text field.
o	Optional field.
o	Represents the description of the restaurant.
•	rating
o	A decimal field.
o	It stores a maximum of 3 digits and 2 decimal places.
o	Validations:
	Has a minimum value of 0 with a custom error message "Rating must be at least 0.00."
	Has a maximum value of 5 with a custom error message "Rating cannot exceed 5.00."
o	Represents the rating of the restaurant.

Examples
Test Code - caller.py
from main_app.models import Restaurant
from django.core.exceptions import ValidationError

valid_restaurant = Restaurant(
    name="Delicious Bistro",
    location="123 Main Street",
    description="A cozy restaurant with a variety of dishes.",
    rating=5.00,
)

try:
    valid_restaurant.full_clean()
    valid_restaurant.save()
    print("Valid Restaurant saved successfully!")
except ValidationError as e:
    print(f"Validation Error: {e}")

invalid_restaurant = Restaurant(
    name="A",
    location="A" * 201,
    description="A restaurant with a long name and invalid rating.",
    rating=5.01,
)

try:
    invalid_restaurant.full_clean()
    invalid_restaurant.save()
    print("Invalid Restaurant saved successfully!")
except Exception as e:
    print(f"Validation Error: {e}")
Output
Valid Restaurant saved successfully!
Validation Error: {'name': ['Name must be at least 2 characters long.'], 'location': ['Location cannot exceed 200 characters.'], 'rating': ['Rating cannot exceed 5.00.']}
2.	Menu
In the main_app create an additional model called "Menu" with the following fields:
•	name
o	A character field.
o	It has a maximum length of 100 characters.
o	Represents the name of the menu.
•	description
o	A text field.
o	A custom validator called "validate_menu_categories" that checks if the description field includes each of the categories: "Appetizers", "Main Course", and "Desserts". If any of these categories is missing, a ValidationError should be raised with the message "The menu must include each of the categories "Appetizers", "Main Course", "Desserts"."
o	Represents the content of the menu.
•	restaurant
o	A foreign key field.
o	Establishes a many-to-one relationship with the "Restaurant" model, associating each menu with a restaurant.
o	When a restaurant is deleted, all menus that reference the deleted restaurant should be deleted too.
Examples
Test Code - caller.py
from main_app.models import Restaurant, Menu

# keep the data from the previous exercise, so you can reuse it

valid_menu = Menu(
    name="Menu at The Delicious Bistro",
    description="** Appetizers: **\nSpinach and Artichoke Dip\n** Main Course: **\nGrilled Salmon\n** Desserts: **\nChocolate Fondue",
    restaurant=Restaurant.objects.first(),
)

try:
    valid_menu.full_clean()
    valid_menu.save()
    print("Valid Menu saved successfully!")
except ValidationError as e:
    print(f"Validation Error: {e}")

invalid_menu = Menu(
    name="Incomplete Menu",
    description="** Appetizers: **\nSpinach and Artichoke Dip",
    restaurant=Restaurant.objects.first(),
)

try:
    invalid_menu.full_clean()
    invalid_menu.save()
    print("Invalid Menu saved successfully!")
except ValidationError as e:
    print(f"Validation Error: {e}")
Output
Valid Menu saved successfully!
Validation Error: {'description': ['The menu must include each of the categories "Appetizers", "Main Course", "Desserts".']}
3.	Restaurant Review
In the main_app create an additional model called "RestaurantReview" with the following fields:
•	reviewer_name
o	A character field.
o	It has a maximum length of 100 characters.
o	Represents the name of the author of the review.
•	restaurant
o	A foreign key field.
o	Establishes a many-to-one relationship with the "Restaurant" model, associating each review with a restaurant.
o	When a restaurant is deleted, all reviews that reference the deleted restaurant should be deleted too.
•	review_content
o	A text field.
o	Represents the content of the review.
•	rating
o	A positive integer field.
o	Has a maximum value of 5.
For this model, also define:
•	A default ordering in descending order for the model's database queries on the field "rating".
•	A human-readable name for the model in the admin interface - "Restaurant Review".
•	A human-readable plural name for the model in the admin interface - "Restaurant Reviews".
•	That NO two records for the fields "reviewer_name" and "restaurant" should share the same combination of values.
Examples
Test Code - caller.py
from main_app.models import Restaurant, RestaurantReview
from django.core.exceptions import ValidationError

restaurant1 = Restaurant.objects.create(name="Restaurant A", location="123 Main St.", description="A cozy restaurant", rating=4.88)
restaurant2 = Restaurant.objects.create(name="Restaurant B", location="456 Elm St.",  description="Charming restaurant", rating=3.59)

RestaurantReview.objects.create(reviewer_name="Bob", restaurant=restaurant1, review_content="Good experience overall.", rating=4)
RestaurantReview.objects.create(reviewer_name="Aleks", restaurant=restaurant1, review_content="Great food and service!", rating=5)
RestaurantReview.objects.create(reviewer_name="Charlie", restaurant=restaurant2, review_content="It was ok!", rating=2)

duplicate_review = RestaurantReview(reviewer_name="Aleks", restaurant=restaurant1, review_content="Another great meal!", rating=5)

try:
    duplicate_review.full_clean()
    duplicate_review.save()
except ValidationError as e:
    print(f"Validation Error: {e}")


print("All Restaurant Reviews:")
for review in RestaurantReview.objects.all():
    print(f"Reviewer: {review.reviewer_name}, Rating: {review.rating}, Restaurant: {review.restaurant.name}")
Output
Validation Error: {'__all__': ['Restaurant Review with this Reviewer name and Restaurant already exists.']}
All Restaurant Reviews:
Reviewer: Aleks, Rating: 5, Restaurant: Restaurant A
Reviewer: Bob, Rating: 4, Restaurant: Restaurant A
Reviewer: Charlie, Rating: 2, Restaurant: Restaurant B
4.	Restaurant Review Types
We decided to differentiate two types of restaurant reviews - regular reviews and food critic reviews. In this case, we do not want the base "RestaurantReview" model to have a database table and save data on its own. Also, in the main_app create two additional models called "RegularRestaurantReview" and "FoodCriticRestaurantReview".
The "RegularRestaurantReview" inherits all fields and options from the base model. No additional fields or options are defined in this subclass.
The "FoodCriticRestaurantReview" includes an additional field:
•	food_critic_cuisine_area
o	A character field.
o	It has a maximum length of 100 characters.
o	Represents the cuisine area/specialization of the food critic.
For this model, also define:
•	A default ordering in descending order for the model's database queries on the field "rating".
•	A human-readable name for the model in the admin interface - "Food Critic Review".
•	A human-readable plural name for the model in the admin interface - "Food Critic Reviews".
•	That NO two records for the fields "reviewer_name" and "restaurant" should share the same combination of values.
Examples
Test Code - caller.py
from main_app.models import Restaurant, RegularRestaurantReview, FoodCriticRestaurantReview

restaurant1 = Restaurant.objects.create(name="Restaurant A", location="123 Main St.", description="A cozy restaurant", rating=4.88)
RegularRestaurantReview.objects.create(reviewer_name="Bob", restaurant=restaurant1, review_content="Good experience overall.", rating=4)
RegularRestaurantReview.objects.create(reviewer_name="Aleks", restaurant=restaurant1, review_content="Great food and service!", rating=5)

duplicate_review = RegularRestaurantReview(reviewer_name="Aleks", restaurant=restaurant1, review_content="Another great meal!", rating=5)

try:
    duplicate_review.full_clean()
    duplicate_review.save()
except ValidationError as e:
    print(f"Validation Error: {e}")

print("Regular Restaurant Review:")
print(f"Model Name: {RegularRestaurantReview._meta.verbose_name}")
print(f"Model Plural Name: {RegularRestaurantReview._meta.verbose_name_plural}")

print("Food Critic Restaurant Review:")
print(f"Model Name: {FoodCriticRestaurantReview._meta.verbose_name}")
print(f"Model Plural Name: {FoodCriticRestaurantReview._meta.verbose_name_plural}")
Output
Validation Error: {'__all__': ['Restaurant Review with this Reviewer name and Restaurant already exists.']}
Regular Restaurant Review:
Model Name: Restaurant Review
Model Plural Name: Restaurant Reviews
Food Critic Restaurant Review:
Model Name: Food Critic Review
Model Plural Name: Food Critic Reviews
5.	Menu Review
In the main_app create an additional model called "MenuReview" with the following fields:
•	reviewer_name
o	A character field.
o	It has a maximum length of 100 characters.
o	Represents the name of the author of the review.
•	menu
o	A foreign key field.
o	Establishes a many-to-one relationship with the "Menu" model, associating each review with a menu.
o	When a menu is deleted, all reviews that reference the deleted menu should be deleted too.
•	review_content
o	A text field.
o	Represents the content of the review.
•	rating
o	A positive integer field.
o	Has a maximum value of 5.
For this model, also define:
•	A default ordering in descending order for the model's database queries on the field "rating".
•	A human-readable name for the model in the admin interface - "Menu Review".
•	A human-readable plural name for the model in the admin interface - "Menu Reviews".
•	That NO two records for the fields "reviewer_name" and "menu" should share the same combination of values.
•	An option to improve database query performance when filtering or sorting by "menu". The option must be set to have a custom index name called "main_app_menu_review_menu_id"
6.	Rating and Review Content
As you can see the rating and the review content are part of each type of review. Your task is to create a reusable component that can be mixed into the models "RestaurantReview" and "MenuReview" to add the review-related fields "rating" and "review_content" and their validation rules. Do not forget to add the common meta options of the models related to the review parts.
Examples
Test Code - caller.py
from main_app.models import RegularRestaurantReview, Restaurant, MenuReview, Menu

Restaurant.objects.create(name="Savory Delight", location="456 Elm Avenue", rating=4.2,)
restaurant_from_db = Restaurant.objects.get(name="Savory Delight")
RegularRestaurantReview.objects.create(reviewer_name="Alice", restaurant=restaurant_from_db, rating=4, review_content="Good experience overall.")
review_from_db = RegularRestaurantReview.objects.get(reviewer_name="Alice", restaurant=restaurant_from_db)
print(
    f"Reviewer name: {review_from_db.reviewer_name}\n"
    f"Restaurant: {review_from_db.restaurant.name}\n"
    f"Rating: {review_from_db.rating}\n"
    f"Review content: {review_from_db.review_content}"
)

Menu.objects.create(name="Delightful Food Menu", description="Appetizers:\nSpinach and Artichoke Dip\nMain Course:\nGrilled Salmon\nDesserts:\nChocolate Fondue", restaurant=restaurant_from_db)
menu_from_db = Menu.objects.get(name="Delightful Food Menu")
MenuReview.objects.create(reviewer_name="Lilly", menu=menu_from_db, rating=5, review_content="Delicious food")
menu_review_from_db = MenuReview.objects.get(reviewer_name="Lilly", menu=menu_from_db)
print(
    f"Reviewer name: {menu_review_from_db.reviewer_name}\n"
    f"Menu: {menu_review_from_db.menu.name}\n"
    f"Rating: {menu_review_from_db.rating}\n"
    f"Review content: {menu_review_from_db.review_content}"
)
Output
Reviewer name: Alice
Restaurant: Savory Delight
Rating: 4
Review content: Good experience overall.
Reviewer name: Lilly
Menu: Delightful Food Menu
Rating: 5
Review content: Delicious food



