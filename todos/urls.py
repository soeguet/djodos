from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.todo_index, name='todo_index'),

    path('<int:todo_id>/', views.todo_detail, name='todo_detail'),

    # path('<int:todo_id>/edit/', views.edit_todo, name='edit_todo'),

    path('api/v1/<int:todo_id>/delete/', views.delete_todo, name='delete_todo'),
    path('api/v1/<int:todo_id>/archive/', views.archive_todo, name='archive_todo'),
    path('api/v1/create/', views.create_todo, name='create_todo'),
    path('api/v1/all_todos/', views.todo_list, name='all_todos'),
]

