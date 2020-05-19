from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('shop:product_list',args=[str(self.id)])


    
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    image = models.ImageField(upload_to='products')
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.SmallIntegerField(null=True,blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[str(self.id)])
