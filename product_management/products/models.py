from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name


class Image(models.Model):
    image_file = models.ImageField(upload_to='product_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    in_stock = models.BooleanField(verbose_name='In Stock?')
    categories = models.ForeignKey(to=Category, null=True   ,on_delete=models.SET_NULL)
    images = models.ManyToManyField(Image, related_name='products', blank=True)

    def __str__(self) -> str:
        return self.name
