# Generated by Django 4.1.6 on 2023-02-10 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_remove_cart_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
