from django import forms
from django.contrib.auth import get_user_model

from gallery.models import Post

User = get_user_model()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("author",)
        widgets = {
            "pub_date": forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S',
                                            attrs={"type": "datetime-local"})
        }
