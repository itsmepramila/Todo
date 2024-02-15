from todo_app import views
from django.urls import path

urlpatterns = [
    path('',views.todo_list, name="todo-list"),
    path('todo-create/', views.todo_create, name="todo-create"),
    path('todo-delete/<int:pk>/', views.todo_delete, name="todo-delete"),
    path('todo-update/<int:pk>/', views.todo_update, name="todo-update"),
]