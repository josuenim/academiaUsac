# Generated by Django 4.2.6 on 2023-10-20 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0004_alter_profesor_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='category',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
