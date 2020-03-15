from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms

class BulkRenameForm(forms.Form):
    # listA = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols':100}), label="Enter list A", max_length=99999) # If you want to control rows and columns
    # listB = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols':100}), label="Enter list B", max_length=99999)

    listA = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'exampleFormControlTextarea3'}), label="Current File Names", max_length=99999)
    listB = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'exampleFormControlTextarea3'}), label="New File Names", max_length=99999)

    directory = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Folder with files to rename'}))

    def __init__(self, *args, **kwargs):
        ''' remove any labels here if desired
        '''
        super(BulkRenameForm, self).__init__(*args, **kwargs)

        self.fields['directory'].label = 'Directory Path'

class JsonMakerForm(forms.Form):
    # listA = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols':100}), label="Enter list A", max_length=99999) # If you want to control rows and columns
    # listB = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols':100}), label="Enter list B", max_length=99999)

    listA = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'exampleFormControlTextarea3'}), label="Keys", max_length=99999)
    listB = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'exampleFormControlTextarea3'}), label="Values", max_length=99999)