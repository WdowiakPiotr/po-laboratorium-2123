# Generated by Django 4.0.4 on 2022-05-25 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samochody', '0003_rename_samochod_car_rename_diler_dealer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service_history',
            new_name='Service',
        ),
    ]
