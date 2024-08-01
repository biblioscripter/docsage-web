from django.urls import path, include
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('user_form/', views.user_form, name='user_form'),
    path('display_users/', views.display_users, name='display_users')
]
