from .models import Worker
from django import forms


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ('name', 'birthdate', 'address', 'phone', 'email', 'dni', 'deparment', 'image')