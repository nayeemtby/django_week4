from django.shortcuts import render

from tasks.models import Task


def home(req):
    ctx = {'tasks': Task.objects.all()}
    return render(req, 'home.html', ctx)
