# Generated by Django 4.2 on 2023-06-29 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bannos', '0003_remove_banno_nombre_alter_banno_valoracion_general'),
    ]

    operations = [
        migrations.AddField(
            model_name='banno',
            name='num_resennas',
            field=models.IntegerField(default=0),
        ),
    ]