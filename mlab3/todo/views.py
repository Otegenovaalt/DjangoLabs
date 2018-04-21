from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from todo.models import Todo
from todo.serializers import TodoSerializer

@csrf_exempt
def todo_list(request):
	if request.method == "GET":
	    todos = Todo.objects.all()
	    ser = TodoSerializer(todos, many=True)
	    return JsonResponse(ser.data, safe=False)
	elif request.method == "POST":
		data = JSONParser().parse(request)
		ser = TodoSerializer(data=data)
		if ser.is_valid():
			ser.save()
			return JsonResponse(ser.data, status=201)
		return JsonResponse({"error": str(e)}, status=400)
	elif request.method == "DELETE":
		todos = Todo.objects.all()
		ser = TodoSerializer(todos, many=True)
		todos.delete()
		return JsonResponse(ser.data, safe=False)

@csrf_exempt
def todo_detail(request, todo_id):
	try:
		todo = Todo.objects.get(id=todo_id)
	except Exception as e:
		return JsonResponse({"error": str(e)}, status=400)
	if request.method == "GET":
		ser = TodoSerializer(todo)
		return JsonResponse(ser.data, safe=False)
	elif request.method == "PUT":
		data = JSONParser().parse(request)
		ser = TodoSerializer(todo, data=data)
		if ser.is_valid():
			ser.save()
			return JsonResponse(ser.data, status=201)
	elif request.method == "DELETE":	
		todo.delete()
		ser = TodoSerializer(todo)
		return JsonResponse(ser.data, safe=False)

@csrf_exempt
def todo_complete(request):
	if request.method == "GET":
	    todos = Todo.objects.filter(complete=True)
	    ser = TodoSerializer(todos, many=True)
	    return JsonResponse(ser.data, safe=False)
	elif request.method == "POST":  #?????
		data = JSONParser().parse(request)
		ser = TodoSerializer(data=data)
		if ser.is_valid():
			ser.save()
			return JsonResponse(ser.data, status=201)
		return JsonResponse({"error": str(e)}, status=400)
	elif request.method == "DELETE":
		todos = Todo.objects.filter(complete=True)
		ser = TodoSerializer(todos, many=True)
		todos.delete()
		return JsonResponse(ser.data, safe=False)

@csrf_exempt
def todo_priority(request):
  if request.method == "GET":
    todos = Todo.objects.order_by('priority')
    ser = TodoSerializer(todos, many=True)
    return JsonResponse(ser.data, safe=False)