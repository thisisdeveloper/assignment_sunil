from django.forms import ModelForm
from . models import Task
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task','start_date','end_date','details']

        widgets = {
                "start_date": forms.DateInput(attrs={"type": "date"}),
                "end_date": forms.DateInput(attrs={"type": "date"}),
            }
            
class TaskUpdateForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task','start_date','end_date','status','details']

        widgets = {
                "start_date": forms.DateInput(attrs={"type": "date"}),
                "end_date": forms.DateInput(attrs={"type": "date"}),
            }

