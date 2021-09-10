from django import forms
from Dashboard.models import Blog


class BlogForms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('Title', 'Genre', 'Description', 'Poster')
