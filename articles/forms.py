from django import forms
from . import models


class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'slug', 'body', 'thumbnail', 'pic']

class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comments
        fields = ['comment']