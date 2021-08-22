# Generated by Django 3.2.5 on 2021-08-10 11:29

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=25)),
                ('street_address', models.CharField(max_length=50)),
                ('postcode', models.CharField(max_length=25)),
                ('town_or_city', models.CharField(max_length=50)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
    ]