from django import forms
from . models import Snippet

class CodeForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('title', 'code', 'linenos', 'language', 'style', )