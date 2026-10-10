from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from videos import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),

    path(
        "accounts/login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login",
    ),

    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),

    path("accounts/signup/", views.signup, name="signup"),
]
