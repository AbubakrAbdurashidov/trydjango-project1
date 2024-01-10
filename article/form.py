from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder':'title'
        })

        self.fields['content'].widget.attrs.update({
            'cols':60,
            'rows':5,
            'placeholder':'content'
        })
            