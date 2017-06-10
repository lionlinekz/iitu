from django import forms

class EticketForm(forms.Form):
    docfile = forms.FileField(
        label='Select a pdf file',
        help_text='max. 42 megabytes'
    )