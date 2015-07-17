from django import forms
from models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'datetime']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['author', 'datetime', 'post']
        # widgets = {
        #     'text': forms.TextInput(
        #         attrs={'id': 'comment_text', 'required': True, 'placeholder': 'Say something...'}
        #     ),
        # }