from django.shortcuts import render
from django.views.generic import TemplateView


def build_home(request):

    return render(request, 'core/index.html')

