
from django import forms
from .models import BlogPost
from ckeditor.widgets import CKEditorWidget

class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = BlogPost
        fields = ['title','content','status']
