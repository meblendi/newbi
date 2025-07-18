from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.create_or_update_user, name='create_or_update_user'),
    path('users/avatar/', views.update_avatar, name='update_avatar'),
]