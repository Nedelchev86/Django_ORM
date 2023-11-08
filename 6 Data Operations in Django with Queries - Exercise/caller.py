import os
import django
from django.db.models import F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


# Create queries within functions
def create_pet(name: str, species: str):
    Pet.objects.create(name=name, species=species)
    return f"{name} is a very cute {species}!"


# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact.objects.create(name=name, origin=origin, age=age, description=description, is_magical=is_magical)
    return f"The artifact {name} is {age} years old!"


def delete_all_artifacts():
    Artifact.objects.all().delete()


# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
#
# print(create_artifact('Crystal Amulet', 'Mystic Forest', 300, 'A magical amulet believed to bring good fortune', True))

def show_all_locations():
    locations = Location.objects.all().order_by("-id")
    return "\n".join(str(loc) for loc in locations)


def new_capital():
    capital = Location.objects.first()
    capital.is_capital = True
    capital.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values("name")


def delete_first_location():
    Location.objects.first().delete()


# Location.objects.create(name="Sofia", population="1329000", region="Sofia Region", description="The capital of Bulgaria and the largest city in the country", is_capital="False")
# Location.objects.create(name="Plovdiv", population="346942", region="Plovdiv Region", description="The second-largest city in Bulgaria with a rich historical heritage", is_capital="False")
# Location.objects.create(name="Varna", population="330486", region="Varna Region", description="A city known for its sea breeze and beautiful beaches on the Black Sea", is_capital="False")


# Car.objects.create(model="Mercedes C63 AMG", year="2019", color="white", price="120000.00")
# Car.objects.create(model="Audi Q7 S line", year="2023", color="black", price="183900.00")
# Car.objects.create(model="Chevrolet Corvette", year="2021", color="dark grey", price="199999.00")

def apply_discount():
    all_cars = Car.objects.all()

    for car in all_cars:
        discount = sum([int(x) for x in str(car.year)])
        price_with_discount = float(car.price) * ((100 - discount)/100)
        car.price_with_discount = price_with_discount
        car.save()

def get_recent_cars():
    all_cars = Car.objects.all().filter(year__gte=2020).values("model", "price_with_discount")
    return all_cars


def delete_last_car():
    Car.objects.last().delete()


# Task.objects.create(title="Sample Task", description="This is a sample task description", due_date="2023-10-31")
# Task.objects.create(title="Sample Task2", description="This is a sample task description2", due_date="2022-10-31", is_finished=True)
# Task.objects.create(title="Sample Task3", description="This is a sample task description3", due_date="2020-10-31")
# Task.objects.create(title="Sample Task4", description="This is a sample task description4", due_date="2024-10-31", is_finished=True)


def show_unfinished_tasks():
    # print([str(task) for task in Task.objects.all().filter(is_finished=False)])
    return "\n".join([str(task) for task in Task.objects.all().filter(is_finished=False)])


def complete_odd_tasks():
    for task in Task.objects.all():
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str):

    encoded = "".join([chr(ord(t) - 3) for t in text])
    Task.objects.filter(title=task_title).update(description=encoded)


    # tasks = Task.objects.filter(title=task_title)
    #
    # for task in tasks:
    #     task.description = encoded
    #     task.save()




    # for task in Task.objects.all():
    #     if task.title == task_title:
    #         task.description = encoded
    #         task.save()


# HotelRoom.objects.create(room_number="101", room_type="Standard", capacity="2", amenities="Tv", price_per_night="100.00")
# HotelRoom.objects.create(room_number="201", room_type="Deluxe", capacity="3", amenities="Wi-Fi", price_per_night="200.00")
# HotelRoom.objects.create(room_number="501", room_type="Deluxe", capacity="6", amenities="Jacuzzi", price_per_night="400.00")


def get_deluxe_rooms():
    deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")

    return "\n".join(str(room) for room in deluxe_rooms if room.id %2 == 0)


def increase_room_capacity():
    previous_room = None

    for room in HotelRoom.objects.all().order_by("id"):
        if not room.is_reserved:
            continue
        if previous_room:
            room.capacity += previous_room
        else:
            room.capacity += room.id
        previous_room = room.capacity
        room.save()


def reserve_first_room():
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room():
    HotelRoom.objects.last().delete()


def update_characters():
    # for character in Character.objects.all():
    #     if character.class_name == "Mage":
    #         character.level += 3
    #         character.intelligence -= 7
    #     elif character.class_name == "Warrior":
    #         character.dexterity += 4
    #         character.hit_points /= 2
    #     else:
    #         character.inventory = "The inventory is empty"
    #     character.save()
    Character.objects.all().filter(class_name="Mage").update(
        level=F("level") + 3,
        intelligence=F("intelligence") - 7
    )
    Character.objects.all().filter(class_name="Warrior").update(
        dexterity=F("dexterity") + 4,  hit_points=F("hit_points") / 2
    )

    Character.objects.all().filter(class_name__in=["Assassin", "Scout"]).update(
        inventory="The inventory is empty"
    )


def fuse_characters(first_character, second_character):
    inventory_str = "Dragon Scale Armor, Excalibur"

    if (first_character.class_name == "Scout" or first_character.class_name == "Mage"):
        inventory_str = "Bow of the Elven Lords, Amulet of Eternal Wisdom"

    Character.objects.create(
        name=f"{first_character.name} {second_character.name}",
        class_name="Fusion",
        level= (first_character.level + second_character.level)//2,
        strength= (first_character.strength + second_character.strength) * 1.2,
        dexterity= (first_character.dexterity + second_character.dexterity) * 1.4,
        intelligence= (first_character.intelligence + second_character.intelligence) * 1.5,
        hit_points= (first_character.hit_points + second_character.hit_points),
        inventory= inventory_str
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.all().update(dexterity=30)


def grand_intelligence():
    Character.objects.all().update(intelligence =40)


def grand_strength():
    Character.objects.all().update(strength=50)


def delete_characters():
    Character.objects.all().filter(inventory="The inventory is empty").delete()




# character1 = Character.objects.create(
#     name="Gandalf",
#     class_name="Mage",
#     level=10,
#     strength=15,
#     dexterity=20,
#     intelligence=25,
#     hit_points=100,
#     inventory="Staff of Magic, Spellbook",
# )
#
# character2 = Character.objects.create(
#     name="Hector",
#     class_name="Warrior",
#     level=12,
#     strength=30,
#     dexterity=15,
#     intelligence=10,
#     hit_points=150,
#     inventory="Sword of Troy, Shield of Protection",
# )
#
# fuse_characters(character1, character2)
# fusion = Character.objects.filter(class_name='Fusion').get()
#
# print(fusion.name)
# print(fusion.class_name)
# print(fusion.level)
# print(fusion.intelligence)
# print(fusion.inventory)
# print(fusion.dexterity)
# print(fusion.strength)
