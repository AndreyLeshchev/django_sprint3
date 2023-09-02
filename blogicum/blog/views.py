from django.shortcuts import get_object_or_404, render

from datetime import datetime as dt

from blog.models import Post, Category

from django.http import Http404


def index(request):
    templates_name = 'blog/index.html'
    post_list = Post.objects.filter(
        pub_date__lt=dt.now(),
        is_published=True,
        category__is_published=True).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, templates_name, context)


def post_detail(request, post_id):
    templates_name = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.filter(
        pub_date__lt=dt.now(),
        is_published=True,
        category__is_published=True),
        pk=post_id
    )
    context = {'post': post}
    return render(request, templates_name, context)


def category_posts(request, category_slug):
    templates_name = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(
        slug=category_slug,
        is_published=True)
    )
    post_list = Post.objects.filter(
        pub_date__lt=dt.now(),
        is_published=True,
        category__slug=category_slug,
    )
    contex = {'category': category,
              'post_list': post_list,
    }
    return render(request, templates_name, contex)
