from django.urls import path
from users.views import SignupView, LoginView

urlpatterns = [
    path("register/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
]
