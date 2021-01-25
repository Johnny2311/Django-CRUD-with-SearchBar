from .models import Worker
from django import forms


class WorkerForm(forms.ModelForm):
    birthdate = forms.DateField(input_formats=['%d/%m/%Y'])
    class Meta:
        model = Worker
        fields = ('__all__')