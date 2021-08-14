# Generated by Django 3.2.5 on 2021-08-14 06:32

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_auto_20210804_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=25, null=True)),
                ('street_address', models.CharField(max_length=50, null=True)),
                ('postcode', models.CharField(max_length=25, null=True)),
                ('town_or_city', models.CharField(max_length=50, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_size', models.CharField(max_length=2)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
