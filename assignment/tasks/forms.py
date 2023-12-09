from django import forms
from task_category.models import TaskCategory

from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = '__all__'
        exclude = ['isComplete',]

    categories = forms.ModelMultipleChoiceField(
        queryset=TaskCategory.objects.all(),
        to_field_name='name',
        required=True,  
        widget=forms.CheckboxSelectMultiple()
    )
    assignedDate = forms.DateField(
        widget=forms.NumberInput({'type':'date'}),
        label='Assigned Date'
    )