from django import forms
from .models import Post


class ReportPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of report...'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell me your story of fishing ...'}),
        }
