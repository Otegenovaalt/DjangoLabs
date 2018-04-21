from django.shortcuts import render, redirect
from django.http import HttpResponse

from todos.models import Todo 

def index(request):
	todos = Todo.objects.all()
	context = {
		'todos': todos
	}
	return render(request, 'index.html', context)

def todo_detail(request, todo_id):
	todo = Todo.objects.get(id=todo_id)
	context = {
		'todo': todo
	}
	return render(request, 'todo_edit.html', context)

def add(request):
	if(request.method == 'POST'):
		title = request.POST['title']
		priority = request.POST['priority']
		todo = Todo(title = title, priority = priority)
		todo.save()
		return redirect('/todos')
	else:
		return render(request, 'add.html')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def deleteTodo(request, todo_id):
	todo = Todo.objects.get(id = todo_id)
	todo.delete()

	return redirect('index')


def editTodo(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    if request.method == "POST":
    	title = request.POST['title']
    	priority = request.POST['priority']
    	todo.title = title
    	todo.priority = priority
    	todo.save()
    	return redirect('index') 
    else:
    	return render(request, 'todo_edit.html')


def sortByDate(request):
	allTodo = Todo.objects.all().order_by('created_at')
	return render(request, 'todo_list.html', {"todo_list": allTodo})

def sortByName(request):
	allTodo = Todo.objects.all().order_by('title')
	return render(request, 'todo_list.html', {"todo_list": allTodo})

def completedList(request):
	allTodo = Todo.objects.all().filter(complete = True)
	return render(request, 'todo_list.html', {"todo_list": allTodo})

def sortByPriority(request):
	allTodo = Todo.objects.all().order_by('priority')
	return render(request, 'todo_list.html', {"todo_list": allTodo})
