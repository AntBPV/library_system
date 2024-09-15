#imports
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.db.models import Q

#making user
User = settings.AUTH_USER_MODEL

## Plugging search app
class BookPostQuerySet(models.QuerySet):
    
    def search(self,query):
        lookup = (
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(user__username__icontains=query)
        )    
        return self.filter(lookup)

class BookPostManager(models.Manager):
    def get_queryset(self):
        return BookPostQuerySet(self.model, using=self._db)
    
    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)

# Create your models here.
class BookPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True,on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='image/',blank=True, null=True)
    doc = models.FileField(upload_to='docs/',blank=True, null=True)
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=300, default='')
    slug = models.SlugField(unique=True, max_length=200)
    content=models.TextField(blank=True, null=True)
    
    NORMAL=0
    SAVED=1
    STATUS_CHOICES= (
        (NORMAL, 'Normal'),
        (SAVED,'Saved'),
    )
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    
    objects = BookPostManager()
    
    def get_absolute_url(self):
        return f"/book/{self.slug}"
    
    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"
    
    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
        
    def get_status(self):
        if self.status==0:
            return True
        else:
            return False
    
    def change_status(self):
        self.status=1
        self.save()
        return f"/book/"
    def remove_status(self):
        self.status=0
        self.save()
        return f"/book/"
