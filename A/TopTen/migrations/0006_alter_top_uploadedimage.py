# Generated by Django 4.0.2 on 2022-02-11 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TopTen', '0005_rename_image_top_uploadedimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='top',
            name='uploadedImage',
            field=models.ImageField(height_field=100, upload_to=''),
        ),
    ]
