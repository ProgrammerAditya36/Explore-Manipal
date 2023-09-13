from django.forms import ModelForm
from django import forms
from .models import User_Events


class UserEventAdd(ModelForm):
    class Meta:
        model = User_Events
        fields = ['name', 'description', 'image', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserEventAdd, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


