# Generated by Django 4.2.6 on 2023-11-22 20:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_catedratico_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='catedratico',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='catedratico',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='catedratico',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]