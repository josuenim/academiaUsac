# Generated by Django 4.2.6 on 2023-11-22 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('accounts', '0004_catedratico_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account',
            new_name='Accounts',
        ),
    ]