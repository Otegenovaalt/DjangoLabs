from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from contact.models import Contact
from contact.serializers import ContactSerializer

@csrf_exempt
def contact_list(request):
	if request.method == "GET":
	    contacts = Contact.objects.all()
	    ser = ContactSerializer(contacts, many=True)
	    return JsonResponse(ser.data, safe=False)
	elif request.method == "POST":
		data = JSONParser().parse(request)
		ser = ContactSerializer(data=data)
		if ser.is_valid():
			ser.save()
			return JsonResponse(ser.data, status=201)
		return JsonResponse({"error": str(e)}, status=400)
	elif request.method == "DELETE":
		contacts = Contact.objects.all()
		ser = ContactSerializer(contacts, many=True)
		contacts.delete()
		return JsonResponse(ser.data, safe=False)

@csrf_exempt
def contact_detail(request, contact_id):
	try:
		contact = Contact.objects.get(id=contact_id)
	except Exception as e:
		return JsonResponse({"error": str(e)}, status=400)
	if request.method == "GET":
		ser = ContactSerializer(contact)
		return JsonResponse(ser.data, safe=False)
	elif request.method == "PUT":
		data = JSONParser().parse(request)
		ser = ContactSerializer(contact, data=data)
		if ser.is_valid():
			ser.save()
			return JsonResponse(ser.data, status=201)
	elif request.method == "DELETE":	
		contact.delete()
		ser = ContactSerializer(contact)
		return JsonResponse(ser.data, safe=False)