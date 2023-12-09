from django.urls import path

from tasks.views import addTask, completeTask, deleteTask, editTask


urlpatterns = [
    path('add', addTask, name='addTask'),
    path('edit/<id>', editTask, name='editTask'),
    path('delete/<id>', deleteTask, name='deleteTask'),
    path('complete/<id>', completeTask, name='completeTask'),
]
