from django.shortcuts import render

from blog.models import Post

from django.http import Http404


def index(request):
    templates_name = 'blog/index.html'
    post_list = Post.objects.all()
    context = {'post_list': post_list}
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
