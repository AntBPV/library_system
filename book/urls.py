from django.urls import path
from .views import (
    book_post_list_view,
    book_post_detail_view,
    book_post_update_view,
    book_post_delete_view
)

urlpatterns = [
    path('<str:slug>/',book_post_detail_view),
    path('',book_post_list_view),
    path('<str:slug>/edit',book_post_update_view),
    path('<str:slug>/delete',book_post_delete_view)
]
