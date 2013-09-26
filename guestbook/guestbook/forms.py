from django import forms
from .models import GuestBook

class GuestbookForm(forms.ModelForm):

    class Meta:
        model = GuestBook 
