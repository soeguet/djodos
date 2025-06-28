# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})


def todo_detail(request, todo_id: int):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'todos/todo_detail.html', {'todo': todo})


def create_todo(request):
    return HttpResponse("Neues Todo erstellen")


def delete_todo(request, todo_id: int):
    delete_count, _ = Todo.objects.filter(id=todo_id).delete()

    if delete_count == 0:
        return HttpResponse(f"Todo {todo_id} nicht gefunden", status=404)

    return render(request, "todos/response/delete_success.html", {'todo_id': todo_id})
