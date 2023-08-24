from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('Welcome/', views.welcome),
    path('Register/', views.registration),
    path('Login/', views.login),
    path('Logout/', views.logout),
    path('UserList/', views.userList),
    path('Edit/<int:id>/', views.display),
]
