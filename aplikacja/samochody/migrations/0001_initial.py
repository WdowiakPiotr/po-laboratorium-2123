# Generated by Django 4.0.4 on 2022-05-25 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Samochod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=50)),
                ('rok_produkcji', models.IntegerField(default=0)),
                ('kolor', models.CharField(max_length=20)),
                ('rodzaj_paliwa', models.CharField(max_length=6)),
                ('moc_silniak', models.IntegerField(default=0)),
            ],
        ),
    ]