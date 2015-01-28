from django.shortcuts import render, HttpResponse, redirect
from django.views import generic


class About(generic.TemplateView):
    template_name = 'static_pages/about.html'