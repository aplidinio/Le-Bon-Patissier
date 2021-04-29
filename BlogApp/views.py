from django.shortcuts import render
from BlogApp.models import Post, Category

# Create your views here.

def blog(request):

    posts = Post.objects.all()
    return render(request, "BlogApp/blog.html", {"posts": posts})

def category(request, category_id):

    category = Category.objects.get(id = category_id)
    post = Post.objects.filter(categories = category)
    return render(request, "BlogApp/category.html", {'category': category, 'posts': post})