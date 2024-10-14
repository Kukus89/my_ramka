from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

User = get_user_model()


class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", )

    def clean(self) -> dict[str, Any]:
        if self.cleaned_data["email"] == self.cleaned_data["username"]:
            raise ValidationError("Email and username must be different")
        return super().clean()
