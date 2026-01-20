from django.urls import path
from .views import *

urlpatterns = [
    path('', blog_page, name='blog'),
    path('<int:post_id>/', post_page, name='post'),
]