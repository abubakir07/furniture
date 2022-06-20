from django.urls import path
from apps.product.views import *


urlpatterns = [

    path('', index, name='index.html'),
    path('', category_product, name='homemain' ),
    path('category/', category_html, name='category.html'),
    path('about_html/', about_html, name='about_html'),
    path('article.html/', article_html, name='article.html'),
    path('blog_1.html/', blog_1_html, name='blog_1.html'),
    path('blog_grid.html/', blog_grid_html, name='blog_grid.html'),
    path('contact/', contact_html, name='contact.html'),
    path('ideas.html/', ideas_html, name='ideas.html'),
    path('product.html/', product_html, name='product.html'),
    path('products_grid.html/', products_grid_html, name='products_grid.html'),
    path('products_list.html/', products_list_html, name='products_list.html'),
    
    
]