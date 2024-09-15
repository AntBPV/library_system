"""
URL configuration for library_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from book.views import (
    book_post_create_view,
    favorite_book_list
)

from searches.views import search_view
from .views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('book/',include('book.urls')),
    path('book-new/',book_post_create_view),
    path('search/', search_view),
    path('favorites/',favorite_book_list)
]
if settings.DEBUG:
    #test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
