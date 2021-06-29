from django.urls import path
from user import views

urlpatterns = [
    path("signup", views.signupUser),
    path("login", views.loginUser),
    path("logout", views.logoutUser),
]
