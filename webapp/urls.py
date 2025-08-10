from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),

    
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('posts/', views.post_list, name='post_list'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<int:pk>/edit/', views.post_update, name='post_update'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),
]
    
