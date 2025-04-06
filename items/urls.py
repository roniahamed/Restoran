from django.urls import path 
from . import views

app_name = 'items'

urlpatterns=[
    path('',views.ItemViews.as_view(), name="show")
]