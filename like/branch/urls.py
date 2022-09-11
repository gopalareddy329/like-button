from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('login/',views.loginuser,name="loginuser"),
    path('logout/',views.logoutuser,name="logoutuser"),
    path('like/<str:no>/',views.like,name="like"),
]