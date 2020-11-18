from django.forms import ModelForm
from .models import Description


class JobForm(ModelForm):
    class Meta:
        model = Description
        fields = ['description']
        exclude = ['title', 'jobs']