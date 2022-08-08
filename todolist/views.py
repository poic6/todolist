from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from django.utils import timezone

# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    context = {'todo_list':todo_list}
    return render(request, 'todolist/index.html', context)

def delete(request, todo_id):
    delete_id = get_object_or_404(Todo, pk=todo_id)
    delete_id.delete()
    return redirect('/todolist/')

def add(request):
    q = Todo(todo=request.POST.get('todo'), is_complete='0', create_date=timezone.now())
    q.save()
    return redirect('/todolist/')

def complete(request, todo_id):
    complete_id = get_object_or_404(Todo, pk=todo_id)
    complete_id.is_complete = 1
    complete_id.save()
    return redirect('/todolist/')

def cancel(request, todo_id):
    cancel_id = get_object_or_404(Todo, pk=todo_id)
    cancel_id.is_complete = 0
    cancel_id.save()
    return redirect('/todolist/')