from django import forms
from .models import Blog
from ckeditor.widgets import CKEditorWidget

class BlogForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=255
    )
    content = forms.CharField(
        widget=CKEditorWidget(),
        max_length=4000
    )
    class Meta:
        model = Blog
        fields = ['title' , 'content']

