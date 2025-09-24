from django.urls import path
from django.views import View
from .import views

urlpatterns = [
    path('',views.Home,name='Homepage')
]
