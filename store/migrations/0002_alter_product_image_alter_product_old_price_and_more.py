# Generated by Django 4.2 on 2023-04-29 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
