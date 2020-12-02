from django import forms
from .models import *

# set forms
class MessageModelForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'