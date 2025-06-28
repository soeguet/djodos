from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),                    # /todos/
    path('create/', views.create_todo, name='create_todo'),         # /todos/create/
    path('<int:todo_id>/', views.todo_detail, name='todo_detail'),  # /todos/5/
    # path('<int:todo_id>/edit/', views.edit_todo, name='edit_todo'), # /todos/5/edit/
    path('<int:todo_id>/delete/', views.delete_todo, name='delete_todo'), # /todos/5/delete/
]