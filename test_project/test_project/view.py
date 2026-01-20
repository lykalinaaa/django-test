from django.shortcuts import render

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

# Главная
def main_page(request):
    data = {"menu": menu, "blog": "/blog/", "post": "/blog/post/"}

    return render(request, "index.html", context=data)

# О блоге
def blog_page(request):
    data = {"menu": menu, "post": "/blog/post/"}

    return render(request, "blog.html", context=data)

# Пост
def post_page(request):
    data = {"menu": menu}

    return render(request, "post.html", context=data)