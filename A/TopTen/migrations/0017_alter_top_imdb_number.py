# Generated by Django 4.0.2 on 2022-02-15 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TopTen', '0016_top_name_dirctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='top',
            name='Imdb_number',
            field=models.FloatField(default=0),
        ),
    ]