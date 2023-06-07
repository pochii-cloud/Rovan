from django.contrib import admin

# Register your models here.
from supplies.models import Supplies, Suppliers

admin.site.register(Supplies)
admin.site.register(Suppliers)
