from django.urls import path 
from . import views

app_name = 'users'

urlpatterns=[
    path('register/',views.CreateUser, name="register"),
    path('login/',views.Login,name='login'),
]