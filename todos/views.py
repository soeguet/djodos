from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

def create_todo(request):
    return HttpResponse("Neues Todo erstellen")


def delete_todo(request, id):
    return HttpResponse(f"Todo {id} löschen")
