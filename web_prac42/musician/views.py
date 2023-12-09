from django.shortcuts import render

# Create your views here.


def addMusician(req):
    return render(req, 'musician_form.html')


def editMusician(req):
    return render(req, 'musician_form.html')


def deleteMusician(req):
    return render(req, 'musician_form.html')
