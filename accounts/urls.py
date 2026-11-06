from django.contrib.auth import views as auth_views
from django.urls import path

from .forms import BootstrapAuthenticationForm
from .views import ProfileUpdateView, SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", ProfileUpdateView.as_view(), name="profile"),
    path(
        "login/",
        auth_views.LoginView.as_view(authentication_form=BootstrapAuthenticationForm),
        name="login",
    ),
]
