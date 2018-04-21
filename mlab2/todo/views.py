from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, QueryDict
from todo.models import Todo

@csrf_exempt 
def todo_list(request):
  if request.method == "GET":
    todos = Todo.objects.all()
    todos_json = [todo.to_json() for todo in todos]
    return JsonResponse(todos_json, safe=False) 
  elif request.method == "POST":
    todo = Todo()
    todo.title = request.POST.get('title', '')
    todo.priority = request.POST.get('priority', '')
    todo.save()   
    return JsonResponse(todo.to_json(), status=201)
  elif request.method == "DELETE":
    todos = Todo.objects.all()
    todos.delete()
    todos_json = [todo.to_json() for todo in todos]
    return JsonResponse(todos_json, safe=False) 

@csrf_exempt
def todo_priority(request):
  if request.method == "GET":
    todos = Todo.objects.order_by('priority')
    todos_json = [todo.to_json() for todo in todos]
    return JsonResponse(todos_json, safe=False) 
  

@csrf_exempt
def todo_complete(request):
  if request.method == "GET":
    todos = Todo.objects.filter(complete=True)
    todos_json = [todo.to_json() for todo in todos]
    return JsonResponse(todos_json, safe=False) 
  elif request.method == "POST":
    todo = Todo()
    todo.title = request.POST.get('title', '')
    todo.priority = request.POST.get('priority', '')
    todo.complete = request.POST.get(False, True) 
      
    todo.save()   
    return JsonResponse(todo.to_json(), status=201)
  elif request.method == "DELETE":
    todos = Todo.objects.filter(complete=True)
    todos.delete()
    todos_json = [todo.to_json() for todo in todos]
    return JsonResponse(todos_json, safe=False)

@csrf_exempt
def todo_detail(request, todo_id):  
    try:
      todo = Todo.objects.get(id=todo_id)
    except Exception as e:
      return JsonResponse({"error": str(e)}, status=400)

    if request.method == "GET":
      return JsonResponse(todo.to_json())
    elif request.method == "PUT":
      data = QueryDict(request.body)
      todo.title = data.get('title', todo.title)
      todo.priority = data.get('priority', todo.priority)
      todo.complete = data.get('complete', todo.complete)
      todo.save()
      return JsonResponse(todo.to_json(), status=201)
    elif request.method == "DELETE":
      todo.delete()
      return JsonResponse(todo.to_json(), status=201)
