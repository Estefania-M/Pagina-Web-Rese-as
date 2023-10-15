# Generated by Django 4.2 on 2023-06-28 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bannos', '0002_alter_ubicacion_edificio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banno',
            name='nombre',
        ),
        migrations.AlterField(
            model_name='banno',
            name='valoracion_general',
            field=models.FloatField(default=1.0),
        ),
    ]
