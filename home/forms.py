from django import forms
from .models import items


class AddItem(forms.ModelForm):

    class Meta:
        model = items
        fields = "__all__"
