from django.core.exceptions import ValidationError


def validate_menu_categories(description):
    for el in ["Appetizers", "Main Course", "Desserts"]:
        if el not in description:
            raise ValidationError('The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')