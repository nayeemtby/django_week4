from django.shortcuts import render

from form_pract.forms import PracticeForm

# Create your views here.

def home(req):
    form = PracticeForm()
    ctx = {
        'form': form,
    }
    return render(req,'index.html',ctx)