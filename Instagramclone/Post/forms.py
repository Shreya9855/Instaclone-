from dataclasses import field, fields
from django import forms
from .models import Posts,Comment

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['post','text']

class NewCommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is in your mind?'}
        )
    )
    class Meta:
        model : Comment
        field = ['comment']