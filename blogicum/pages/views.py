from django.shortcuts import render


def about(request):
    templates_name = 'pages/about.html'
    return render(request, templates_name)


def rules(request):
    templates_name = 'pages/rules.html'
    return render(request, templates_name)
