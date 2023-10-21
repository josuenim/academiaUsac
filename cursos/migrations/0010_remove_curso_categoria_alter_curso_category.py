# Generated by Django 4.2.6 on 2023-10-20 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('cursos', '0009_curso_categoria_alter_curso_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='categoria',
        ),
        migrations.AlterField(
            model_name='curso',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categorias.categorias'),
        ),
    ]
