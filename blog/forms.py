from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','meta_description', 'link',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title'}),
            'text': forms.Textarea(attrs={'class': 'text'}),
            'meta_description': forms.TextInput(attrs={'class': 'meta_description'}),
            'link': forms.TextInput(attrs={'class': 'link'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = { 'text': forms.Textarea(attrs={'class': 'comment-text'})}
