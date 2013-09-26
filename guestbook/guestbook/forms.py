"""
A base contact form for allowing users to send email messages through
a web interface, and a subclass demonstrating useful functionality.
"""

from django import forms
from .models import GuestBook

class GuestbookForm(forms.ModelForm):
    
    class Meta:
        model = GuestBook 
