# Generated by Django 4.2.4 on 2023-11-12 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subjects', models.ManyToManyField(to='main_app.subject')),
            ],
        ),
    ]