from django.contrib import admin

# Register your models here.

from apps.product.models import *

admin.site.register(Category)
admin.site.register(Products)