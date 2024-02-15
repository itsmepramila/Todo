from todo_app.models import Todo
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields="__all__"
    
    
    