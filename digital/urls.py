from digital import views
from django.urls import path, include
from digital.views import*

urlpatterns = [
    path('', views.homeindex, name="home"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('mail', views.mail, name="mail"),
    path('geographie', views.geographie, name="geographie")
]