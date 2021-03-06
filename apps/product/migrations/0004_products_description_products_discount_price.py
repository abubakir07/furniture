# Generated by Django 4.0.4 on 2022-06-18 11:07

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_name_category_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='products',
            name='discount_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
