from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from datetime import datetime

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
    data = {"menu": menu, "posts": post, "comments": "/comments/"}

    return render(request, "post.html", context=data)


def comments_page(request, post_id):
    if request.method == 'POST':
        fio = request.POST['fio']
        email = request.POST['email']
        text = request.POST['text']
        created_at = datetime.now()

        formatted = created_at.strftime("%d.%m.%Y %H:%M")

        if fio and email and text:
            Comment.objects.create(fio=fio, email=email, text=text, post_id=post_id, created_at=formatted)
            return redirect('comments', post_id=post_id)

    comments = Comment.objects.filter(post_id=post_id)

    data = {
        "menu": menu,
        "post_id": post_id,
        "comments": comments,
    }

    return render(request, "comments.html", context=data)
