from django import forms

class FileForm(forms.Form):
    file = forms.FileField(help_text="Enter a CNAB file")