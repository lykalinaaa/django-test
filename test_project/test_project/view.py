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