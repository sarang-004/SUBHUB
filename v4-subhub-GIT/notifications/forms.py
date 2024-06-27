from django import forms
from .models import Notification

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['title', 'recipient', 'type', 'details']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'recipient': forms.EmailInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'}),
        }