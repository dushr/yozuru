from django.shortcuts import render, HttpResponse, redirect
from django.views import generic
from api import models


class ProjectIndex(generic.ListView):
    queryset = models.Project.objects.all()
    template_name = "projects/index.html"


class ProjectDetail(generic.DetailView):
    model = models.Project
    template_name = "projects/project.html"
