from . import views
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('', views.home),
    path('signup/', views.signup,name='signup'),
    path('loginn/', views.loginn,name='loginn'),
    path('todopage', views.todo,name='todo'),
    path('delete_todo/<int:srno>', views.delete_todo,name='delete'),
    path('edit_todo/<int:srno>', views.edit_todo, name='edit_todo'),
    path('logout/', views.logout, name='logout'),
    
]