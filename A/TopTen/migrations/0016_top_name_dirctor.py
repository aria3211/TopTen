# Generated by Django 4.0.2 on 2022-02-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TopTen', '0015_top_imdb_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='top',
            name='Name_dirctor',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
