from django.http import HttpResponse
from django.shortcuts import render
import random

from book.models import BookPost

def home_page(request):
    my_title='Sistema de gestion de biblioteca'
    my_content='Por Antonio Parra'
    
    items = list(BookPost.objects.all())
    random_items = random.sample(items,3)
    
    context={"title":my_title, "content":my_content, 'book_list':random_items}
    
    return render(request, "home.html", context)