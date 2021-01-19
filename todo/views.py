from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, "todo/index.html", context)
def show(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, "todo/show.html", {
        'todo': todo
    })

def create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'todo/create.html', {'form' : form})

def update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'todo/create.html', {'form' : form})

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')