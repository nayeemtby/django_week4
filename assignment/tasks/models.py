from django.db import models

from task_category.models import TaskCategory

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=64,verbose_name='Task Title')
    description = models.TextField(verbose_name='Task Description')
    isComplete = models.BooleanField(default=False)
    assignedDate = models.DateField(verbose_name='Assigned Date')
    categories = models.ManyToManyField(TaskCategory,verbose_name='Task Categories')
