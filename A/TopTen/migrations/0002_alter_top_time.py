# Generated by Django 4.0.2 on 2022-02-02 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TopTen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='top',
            name='Time',
            field=models.DateField(),
        ),
    ]