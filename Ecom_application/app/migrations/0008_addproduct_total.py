# Generated by Django 3.2.12 on 2023-01-28 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproduct',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
