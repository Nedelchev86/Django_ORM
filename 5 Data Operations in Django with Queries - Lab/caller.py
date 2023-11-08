import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Student


# def add_students():
#     students = Student(student_id= "FC5204", first_name="John", last_name="Doe", birth_date="1995-05-15", email="john.doe@university.com")
#     students2 = Student(student_id= "FE0054", first_name="Jane", last_name="Smith",  email="jane.smith@university.com")
#     students3= Student(student_id= "FH2014", first_name="Alice", last_name="Johnson", birth_date="1998-02-10", email="alice.johnson@university.com")
#     students4 = Student(student_id= "FH2015", first_name="Bob", last_name="Wilson", birth_date="1996-11-25", email="bob.wilson@university.com")
#     students.save()
#     students2.save()
#     students3.save()
#     students4.save()

def add_students():
    Student.objects.create(student_id="SC5204", first_name="John", last_name="Doe", birth_date="1995-05-15", email="john2.doe@university.com")
    Student.objects.create(student_id="SE0054", first_name="Jane", last_name="Smith",  email="jane2.smith@university.com")
    Student.objects.create(student_id="SH2014", first_name="Alice", last_name="Johnson", birth_date="1998-02-10", email="alice2.johnson@university.com")
    Student.objects.create(student_id="SH2015", first_name="Bob", last_name="Wilson", birth_date="1996-11-25", email="bob2.wilson@university.com")


# Create and check models
# Run and print your queries


# add_students()
# print(Student.objects.all())


def get_students_info():
    allStudents = Student.objects.all()

    return "\n".join([f"Student №{student.student_id}: {student.first_name} {student.last_name}; Email: {student.email}" for student in allStudents])

# print(get_students_info())

def update_students_emails():
    allStudents = Student.objects.all()
    for student in allStudents:
        emails = student.email.replace("university.com", "uni-students.com")
        student.email = emails
        student.save()


# update_students_emails()
# for student in Student.objects.all():
#     print(student.email)

def truncate_students():
    Student.objects.all().delete()


truncate_students()
print(Student.objects.all())
print(f"Number of students: {Student.objects.count()}")
