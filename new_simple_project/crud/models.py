from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=45)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    tag = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pro_img = models.ImageField(upload_to = 'product_folder/%Y/%m/%d/', default = 'product_folder/None/no-img.jpg')