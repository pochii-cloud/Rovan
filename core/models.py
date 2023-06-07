import datetime

import django.utils.timezone
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'


class Sales(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.CharField(max_length=200, default='')
    total_sales = models.PositiveBigIntegerField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.total_sales)

    class Meta:
        verbose_name_plural = 'Sales'
