from datetime import datetime as dt

from django.shortcuts import get_object_or_404, render

from blog.models import Post, Category


def index(request):
    NUMBER_PUBLICATIONS = 5
    templates_name = 'blog/index.html'
    posts = Post.objects.filter(
        pub_date__date__lt=dt.now(),
        is_published=True,
        category__is_published=True,
    ).order_by('-pub_date')[:NUMBER_PUBLICATIONS]
    context = {
        'post_list': posts,
    }
    return render(request, templates_name, context)


def post_detail(request, post_id):
    templates_name = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.filter(
            pub_date__date__lt=dt.now(),
            is_published=True,
            category__is_published=True,
        ),
        pk=post_id,
    )
    context = {
        'post': post,
    }
    return render(request, templates_name, context)


def category_posts(request, category_slug):
    templates_name = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(
            slug=category_slug,
        ),
        is_published=True,
    )
    posts_category = Post.objects.filter(
        pub_date__date__lt=dt.now(),
        is_published=True,
        category__slug=category_slug,
    )
    context = {
        'category': category,
        'post_list': posts_category,
    }
    return render(request, templates_name, context)
