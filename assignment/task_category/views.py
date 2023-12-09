from django.http import HttpRequest, HttpResponseNotAllowed
from django.shortcuts import redirect, render

from task_category.forms import TaskCategoryForm

# Create your views here.

notAllowed = HttpResponseNotAllowed(['GET', 'POST'])

def addTaskCategory(req:HttpRequest):
    ctx: dict[str, object] = {'btnTxt': 'Add Task Category',
                              'title': 'Add'}
    if req.method == 'GET':
        ctx['form'] = TaskCategoryForm()
        return render(req, 'form.html', ctx)
    elif req.method == 'POST':
        form = TaskCategoryForm(req.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
        else:
            ctx['form'] = form
            return render(req, 'form.html', ctx)
    return notAllowed