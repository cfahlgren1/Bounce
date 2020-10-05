from django import forms
from .models import Signup

class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "class" :"input",
        "type" :"email",
        "placeholder" : "e.g. bobsmith@gmail.com",
    }), label='')
    class Meta:
        model = Signup
        fields = ('email',)