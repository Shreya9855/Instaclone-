
from django import forms
from .models import UserModel,PostModel,CommentModel

class newProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('display_name','email','website','profile_pic','bio')



class NewPostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['post','text']

class NewCommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is in your mind?'}
        )
    )
    class Meta:
        model : CommentModel
        field = ['comment']