from django import forms


class FormSupplier(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)


