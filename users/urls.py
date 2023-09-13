from django.urls import path
from . import  views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('', views.profiles, name='profiles'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('edit-account/', views.editAccount, name="edit-account"),


]