from cProfile import label
from statistics import mode
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField



class Category(models.Model):
    title = models.CharField(max_length=140)
    image = models.ImageField(blank=True, null=True)
    icon = models.ImageField(blank=True, null=True)   
    url = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Категории"
        ordering = ['-id']

class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True ,verbose_name='Категория')
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    image = models.ImageField(upload_to=" media/", blank=True, null=True, verbose_name='Картина')
    description = models.CharField(verbose_name='Описание', blank=True, null=True, max_length=300 )
    url = models.SlugField(null=True, unique=True, verbose_name='URL' )
    price = models.DecimalField(decimal_places=2, max_digits=10)
    discount_price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    material = models.CharField(max_length = 100, null = True, blank = True)

    

    def __str__(self):
        return self.title
    
    def get_absolue_url(self):
        return f'update/{self.id}'

    class Meta:
        verbose_name_plural = "Продукты"
        ordering = ['-id']
