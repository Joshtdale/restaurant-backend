# Generated by Django 4.1.3 on 2022-11-09 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='menuItems',
            new_name='MenuItem',
        ),
    ]
