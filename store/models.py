from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    parent = models.ForeignKey('self',on_delete=models.CASCADE, related_name='childdren',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_images',blank=True,null=True)
    slug = models.SlugField(max_length=200,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_product')
    desc = models.TextField(blank=True,null=True)
    price = models.FloatField()
    old_price = models.FloatField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductRelatedImage(models.Model):
    related_img = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='related_product_image')
    image = models.ImageField(upload_to='product_related_images',blank=True,null=True)