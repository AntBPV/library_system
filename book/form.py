from django import forms 
from .models import BookPost
from django.forms import TextInput, Textarea, FileInput

class BookPostForm(forms.Form):
    title= forms.CharField()
    content= forms.CharField(widget=forms.Textarea)
    
class BookPostModelForm(forms.ModelForm):
    class Meta:
        model=BookPost
        fields=['title','image','content','doc','author']
        
        widgets = {
            'title': TextInput(attrs={
                        
                        'style': 'max-width: 300px;',
                        'id': 'FormInputTitle',
                        'placeholder': 'Titulo'
            }),
            'content': Textarea(attrs={
                        
                        'style': 'max-width: 300px;',
                        'rows': 3,
                        'id': 'FormInputContent',
                        'placeholder': 'Descripción'

            }),
            'author': TextInput(attrs={
                        
                        'style': 'max-width: 300px;',
                        'id': 'FormInputAuthor',
                        'placeholder': 'Autor'

            }),
            'image': FileInput(attrs={
                        
                        'style': 'max-width: 300px;',
                        'id': 'FormInputImage'
            }),
            'doc': FileInput(attrs={
                        
                        'style': 'max-width: 300px;',
                        'id': 'FormInputDoc'
            }),
        }
    
    def clean_title(self,*args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = BookPost.objects.filter(title__iexact=title)
        
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        
        if qs.exists():
            raise forms.ValidationError("This title already exists")
        return title 