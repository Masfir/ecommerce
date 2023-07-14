# Generated by Django 4.2 on 2023-05-02 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_image_alter_product_old_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRelatedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_related_images')),
                ('related_img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_product_image', to='store.product')),
            ],
        ),
    ]