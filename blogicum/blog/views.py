from django.shortcuts import render

from django.http import Http404


def index(request):
    templates_name = 'blog/index.html'
    context = {'posts': posts}
    return render(request, templates_name, context)


def post_detail(request, post_id):
    templates_name = 'blog/detail.html'
    try:
        context = {'post': posts[post_id]}
    except IndexError:
        raise Http404('Данный запрошенный объект не существует')
    return render(request, templates_name, context)


def category_posts(request, category_slug):
    templates_name = 'blog/category.html'
    contex = {'category': category_slug}
    return render(request, templates_name, contex)
