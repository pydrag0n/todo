from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.mainpage, name="mainpage"),
    path('todo/<int:id>/delete', views.delete, name="delete"),
    path('todo/<int:id>/update', views.update, name="update"),
    path('todo/add', views.add, name="add")    
]
