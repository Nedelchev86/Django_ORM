# Generated by Django 4.2.4 on 2023-11-09 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_zookeeper_specialty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zookeeper',
            name='specialty',
            field=models.CharField(choices=[('Mammals', 'Mammals'), ('Birds', 'Birds'), ('Reptiles', 'Reptiles'), ('Others', 'Others')], max_length=10),
        ),
    ]
