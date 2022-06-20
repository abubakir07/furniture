from django.shortcuts import redirect, render
from apps.product.forms import  ContactForm
from apps.product.models import *
import datetime
from django.db.models import Q
# from services.send_email import send_email


def index(request):
    icon_category = Category.objects.all()
    product_all = Products.objects.all()


    if 'search_button' in request.GET:  
        product_all = Products.objects.filter(Q(title__icontains=word))
        category_all = Category.object.filter(Q(title__icontains=word))
        return render(request, 'MAIN/header.html', {'news_slider': product_all})
    else:
        category_all = Category.objects.all()
        product_all = Products.objects.all()
        now = datetime.datetime.now()
    context = {    
        'now':now,
        'icon_category': icon_category,
        'category_all': category_all,
        'product_all': product_all
        }
    return render(request, 'MAIN/index.html', context)




def category_product(request, id):
    category_al = Category.objects.all()
    product_al = Products.objects.all()
    context = {
        'category_all':category_al,
        'product_all':product_al,
    }
    return render(request, 'MAIN/main.html', context)



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_email(
                form.cleaned_data['name'],
                form.cleaned_data['email'],
                form.cleaned_data['message']
                )
            
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})  



def category_html(request):
    category_all = Category.objects.all()
    product_all = Products.objects.all()
    context = {
        'category_all':category_all,
        'product_all':product_all,
    }
    return render(request, 'category.html')

def about_html(request):
    return render(request, 'about.html')

def article_html(request):
    return render(request, 'article.html')

def blog_1_html(request):
    return render(request, 'blog_1.html')

def blog_grid_html(request):
    return render(request, 'blog_grid.html')
    
def contact_html(request):
    return render(request, 'contact.html')

def ideas_html(request):
    return render(request, 'ideas.html')

def product_html(request):
    return render(request, 'product.html')

def products_grid_html(request):
    return render(request, 'products_grid.html')

def products_list_html(request):
    return render(request, 'products_list.html')