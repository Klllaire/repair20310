from django import forms
from .models import LogItem

class LogItemForm(forms.ModelForm):
  class Meta:
    model = LogItem
    fields = ['handler', 'status', 'comment']
    widgets = {
      'comment': forms.Textarea(attrs={
        'class': 'form-control', 
        'placeholder': '請在此輸入處理情形...'},
      ),
    }
