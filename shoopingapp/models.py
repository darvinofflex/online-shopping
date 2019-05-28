from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=500)
    slug =models.SlugField(max_length=500)
    class Meta:
        ordering =('name',)
        verbose_name = 'category'
        verbose_name_plural='categories'
    def get_absolute_url(self):
        return reverse('shoopingapp:product_list_by_category',args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=500, db_index=True)
    slug = models.SlugField(max_length=500, db_index=True)
    cover = models.FileField(default=1)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('shoopingapp:product_detail', args=[self.id, self.slug])


