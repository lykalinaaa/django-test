from django.shortcuts import render, get_object_or_404
from .models import Post

# меню для всех страниц
menu = [
        {
            "title": "Главная",
            "link": "/"
        },
        {
            "title": "Блог",
            "link": "/blog/"
        }
    ]

posts = Post.objects.all()

def blog_page(request):
    data = {"menu": menu, "post": "/post/", "posts": posts}

    return render(request, "blog.html", context=data)

# Пост
def post_page(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    data = {"menu": menu, "posts": post}

    return render(request, "post.html", context=data)
