from django.http import HttpRequest, HttpResponseNotAllowed
from django.shortcuts import redirect, render

from tasks.forms import TaskForm
from tasks.models import Task

# Create your views here.

notAllowed = HttpResponseNotAllowed(['GET', 'POST'])

def addTask(req:HttpRequest):
    ctx: dict[str, object] = {'btnTxt': 'Add',
                              'title': 'Add Task'}
    if req.method == 'GET':
        ctx['form'] = TaskForm()
        return render(req, 'form.html', ctx)
    elif req.method == 'POST':
        form = TaskForm(req.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
        else:
            ctx['form'] = form
            return render(req, 'form.html', ctx)
    return notAllowed


def editTask(req,id):
    ctx: dict[str, object] = {
        'btnTxt': 'Update', 'title': 'Edit Task'}
    if req.method == 'GET':
        task = Task.objects.get(pk=id)
        ctx['form'] = TaskForm(instance=task)
        return render(req, 'form.html', ctx)
    elif req.method == 'POST':
        form = TaskForm(req.POST, instance=Task.objects.get(pk=id))
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
        else:
            ctx['form'] = form
            return render(req, 'form.html', ctx)
    return notAllowed


def deleteTask(req,id):
    Task.objects.get(pk=id).delete()
    return redirect('home')


def completeTask(req,id):
    task = Task.objects.get(pk=id)
    task.isComplete=True
    task.save()
    return redirect('home')
