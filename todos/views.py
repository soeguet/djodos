from django.contrib.auth.decorators import login_required
from django.utils import timezone

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from accounts.models import UserProfile
from .models import Todo

### VIEW CALLS ###

def todo_index(request: HttpRequest):
    try:
        active_filter = request.user.userprofile.get_preference('filter', 'active')
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=request.user)
        active_filter = 'active'

    return render(request, 'todos/todo_body.html', {'current_filter': active_filter})


@login_required
def todo_list(request: HttpRequest):

    active_filter = request.GET.get('filter', 'none')

    try:
        theme = request.user.userprofile.get_preference('theme', 'light')
        request.user.userprofile.set_preference('last_visit', str(timezone.now()))

        if active_filter == 'none':
            active_filter = request.user.userprofile.get_preference('filter', 'active')
        else:
            request.user.userprofile.set_preference('filter', active_filter)

    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=request.user)
        theme = 'light'

    print(theme)

    if active_filter == 'active':
        todos = Todo.objects.filter(archived=False, completed=False)
    elif active_filter == 'archived':
        todos = Todo.objects.filter(archived=True)
    else:
        todos = Todo.objects.all()

    return render(request, 'todos/todo_list.html', {'todos': todos,'current_filter': active_filter})


def todo_detail(request: HttpRequest, todo_id: int):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

### API CALLS ###

def create_todo(request: HttpRequest):
    return HttpResponse("Neues Todo erstellen")

def archive_todo(request: HttpRequest, todo_id: int):
    try:
        todo = Todo.objects.get(id=todo_id)
        todo.archived = True
        todo.save()
        return render(request, "todos/response/archive_success.html", {'todo': todo})
    except Todo.DoesNotExist:
        return HttpResponse(f"Todo {todo_id} nicht gefunden", status=404)

def delete_todo(request: HttpRequest, todo_id: int):
    delete_count, _ = Todo.objects.filter(id=todo_id).delete()

    if delete_count == 0:
        return HttpResponse(f"Todo {todo_id} nicht gefunden", status=404)

    return render(request, "todos/response/delete_success.html", {'todo_id': todo_id})
