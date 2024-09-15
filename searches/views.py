from django.shortcuts import render

#models
from book.models import BookPost
from .models import SearchQuery

# Create your views here.
def search_view(request):
    query= request.GET.get('q', None)
    user= None
    
    if request.user.is_authenticated:
        user= request.user
    
    context={"query":query}    
    
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        book_list = BookPost.objects.search(query=query)
        context['book_list'] = book_list
        
    return render(request,'searches/view.html', context)