from django import forms
from .models import Post


class ReportPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tell us about...'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Share your story of fishing ...'}),
        }
