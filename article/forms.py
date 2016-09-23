from django.forms import ModelForm
from django.forms import TextInput, Textarea

from tinymce.widgets import TinyMCE

from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control input-sm'}),
            'body': TinyMCE(attrs={'cols': 80, 'rows': 30, 'class': 'form-control'})
        }