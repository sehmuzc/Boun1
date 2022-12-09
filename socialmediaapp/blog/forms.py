from.models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    body = forms.CharField(label='Your Comment', min_length=1, max_length=300)

    class Meta:
            model = Comment
            fields = ['body']
