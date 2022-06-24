from django import forms
from .models import Comment
from ckeditor.fields import RichTextField

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        content = RichTextField()