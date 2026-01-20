from django.urls import path
from .views import *

urlpatterns = [
    path('', blog_page, name='blog'),  # /blog/
    path('<int:post_id>/', post_page, name='post'),  # /blog/1/
    path('<int:post_id>/comments/', comments_page, name='comments'),  # /blog/1/comments/
]