from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm

from .models import CustomUser


class BootstrapFormMixin:
    """Adds the Bootstrap 5 'form-control' class to every field."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class CustomUserCreationForm(BootstrapFormMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "course")


class BootstrapAuthenticationForm(BootstrapFormMixin, AuthenticationForm):
    pass


class ProfileUpdateForm(BootstrapFormMixin, ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "course")
