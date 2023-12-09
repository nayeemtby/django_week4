from django.urls import path

from task_category.views import addTaskCategory


urlpatterns = [
    path('add', addTaskCategory,name='addTaskCategory'),
]
