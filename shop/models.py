from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name')
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    image = models.ImageField(upload_to='products',blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name