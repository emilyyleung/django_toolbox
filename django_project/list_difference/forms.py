from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms

class ListCheckerForm(forms.Form):
    listA = forms.CharField(widget=forms.Textarea, label="Enter list A", max_length=99999)
    listB = forms.CharField(widget=forms.Textarea, label="Enter list B", max_length=99999)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = "post"