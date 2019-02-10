from django import forms
from .models import Supplier, Site, Contract


class FormSupplier(forms.ModelForm):
    class Meta:
        model = Supplier
        # fields = ("name", "description")
        exclude = ["last_user_modify"]


class FormSite(forms.ModelForm):
    class Meta:
        model = Site
        # fields = "__all__"
        exclude = ["last_user_modify"]


class FormContract(forms.ModelForm):
    class Meta:
        model = Contract
        # fields = "__all__"
        exclude = ["last_user_modify"]
