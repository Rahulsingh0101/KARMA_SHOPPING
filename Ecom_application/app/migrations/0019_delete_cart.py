# Generated by Django 4.1.6 on 2023-02-03 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_delete_orderplaced'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
