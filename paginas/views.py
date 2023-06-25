from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexViews(TemplateView):
    template_name="index.html"

class SuplementoViews(TemplateView):
    template_name="suplemento.html"