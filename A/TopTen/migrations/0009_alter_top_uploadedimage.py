# Generated by Django 4.0.2 on 2022-02-14 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TopTen', '0008_alter_top_uploadedimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='top',
            name='uploadedImage',
            field=models.ImageField(upload_to=''),
        ),
    ]