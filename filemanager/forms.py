from django import forms
from django.forms import ModelForm, Textarea
from .models import FileManageTable
# class FileForm(forms.Form):
#     name = forms.CharField()
#     fileName = forms.FileField()
    
#     email = forms.EmailField()
    
#     password = forms.PasswordInput()

class FileForm(ModelForm):
    class Meta:
        model = FileManageTable
        fields = ('email', 'filename', 'password')
        # widgets = {
        #     'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }

class downloadForm(forms.Form):
    key = forms.IntegerField(max_value=999999)
