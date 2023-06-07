from django.contrib import admin

# Register your models here.
from core.models import Category, Product, Sales

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sales)
