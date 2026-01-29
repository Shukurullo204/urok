from django.shortcuts import render
from django.db.models import Q

from .models import *

def index_view(request):
    categories = Category.objects.all()
    posts = Post.objects.all()

    context = {
        "categories": categories,
        "posts": posts,
        "title": "Главная страница"
    }

    return render(request, "blog/index.html", context)


def about_us_view(request):
    context = {
        "title": "О нас"
    }
    return render(request, "blog/about_us.html", context)

def services_view(request):
    context = {
        "title": "Сервисы"
    }
    return render(request, "blog/services.html", context)

def our_team_view(request):
    context = {
        "title": "Наша команда"
    }
    return render(request, "blog/our_team.html", context)

def contacts_view(request):
    context = {
        "title": "Контакты"
    }
    return render(request, "blog/contacts.html", context)



def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category=category)
    categories = Category.objects.all()

    context = {
        "category": category,
        "posts": posts,
        "categories": categories,
        "title": f"Категория: {category.name}"
    }

    return render(request, "blog/category.html", context)


def post_detail_view(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    tags = post.tags.all()

    posts = Post.objects.all().order_by('-views')[:3]

    context = {
        "post": post,
        "tags": tags,
        "title": f"Пост: {post.title}",
        "posts": posts
    }

    return render(request, "blog/post.html", context)


# Реализовать поиск у себя
# Как я не знаю ?

def search_view(request):
    q = request.GET.get("q")
    posts = Post.objects.filter(
        Q(title__icontains=q) | Q(content__icontains=q)
    )
    context = {
        "q": q,
        "posts": posts,
        "title": f"Результаты поиска !"
    }

    return render(request, "blog/search.html", context)


