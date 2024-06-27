from django import forms
from .models import Scolorship

class ScolorshipForm(forms.ModelForm):
    class Meta:
        model = Scolorship
        fields = "__all__"