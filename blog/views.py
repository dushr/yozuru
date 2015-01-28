from django.shortcuts import render, HttpResponse, redirect
from django.views import generic
from api import models


class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog/index.html"
    paginate_by = 6


class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "blog/post.html"

# Custom error pages


def error404(request):
    return render(request, 'error/lost.html')


def error500(request):
    return render(request, 'error/calamity.html')