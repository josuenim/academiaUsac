# Generated by Django 4.2.6 on 2023-10-21 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorias',
            old_name='slug',
            new_name='category_slug',
        ),
    ]
