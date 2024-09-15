from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404, HttpResponse
from django.core.files import File

from django.shortcuts import render, get_object_or_404, redirect


from .form import BookPostModelForm
from .models import BookPost

# Create your views here.

def book_post_list_view(request):
    qs=BookPost.objects.all()
    if request.user.is_authenticated:
        my_qs=BookPost.objects.filter(user=request.user)
        qs=(qs|my_qs).distinct()
        
    template_name= 'book/list.html'
    context= {'object_list': qs}
    
    return render(request, template_name, context)

def favorite_book_list(request):
    qs=BookPost.objects.filter(status=1)
    template_name='book/list.html'
    context={
        'object_list':qs,
        'title': 'Tus libros favoritos: '
        }
    return render(request,template_name,context)

#CRUD

#Create
def book_post_create_view(request):
    form = BookPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BookPostModelForm()
    template_name= 'form.html'
    context = {
        'title': "Crear libro",
        'form':form
        }
    
    return render(request, template_name, context)
    
    
#Retrieve
def book_post_detail_view(request,slug):
    obj = get_object_or_404(BookPost, slug=slug)
    template_name= 'book/detail.html'
    context = {'object':obj}
    
    return render(request,template_name,context)

#Update            
def book_post_update_view(request,slug):
    obj=get_object_or_404(BookPost,slug=slug)
    form=BookPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        print('form is valid')
        form.save()
    else:
        print('form is not valid')
    template_name = 'form.html'
    context = {"title": f"Update {obj.title}", "form":form}
    
    return render(request,template_name, context) 


#Delete
def book_post_delete_view(request,slug):
    obj = get_object_or_404(BookPost, slug=slug)
    template_name= 'book/delete.html'
    
    if request.method=='POST':
        obj.delete()
        return redirect('/book')
    
    context = {'object': obj}
    
    return render(request,template_name,context)