from django.urls import path
from .views import IndexViews, SuplementoViews
from django.contrib.auth import views as logar

urlpatterns=[
    path("", IndexViews.as_view(), name="index"),
    path("suplemento", SuplementoViews.as_view(), name="suplemento"),
    path("login", logar.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout", logar.LogoutView.as_view(), name="logout"),
]