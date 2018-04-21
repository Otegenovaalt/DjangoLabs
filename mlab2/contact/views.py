from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, QueryDict
from contact.models import Contact

@csrf_exempt 
def contact_list(request):
  if request.method == "GET":
    contacts = Contact.objects.all()
    contacts_json = [contact.to_json() for contact in contacts]
    return JsonResponse(contacts_json, safe=False) 
  elif request.method == "POST":
    contact = Contact()
    contact.firstName = request.POST.get('firstName', '')
    contact.lastName = request.POST.get('lastName', '')
    contact.phone = request.POST.get('phone', '')
    contact.email = request.POST.get('email', '')
    contact.save()   
    return JsonResponse(contact.to_json(), status=201)
  elif request.method == "DELETE":
    contacts = Contact.objects.all()
    contacts.delete()
    contacts_json = [contact.to_json() for contact in contacts]
    return JsonResponse(contacts_json, safe=False)

@csrf_exempt
def contact_detail(request, contact_id):  
    try:
      contact = Contact.objects.get(id=contact_id)
    except Exception as e:
      return JsonResponse({"error": str(e)}, status=400)

    if request.method == "GET":
      return JsonResponse(contact.to_json())
    elif request.method == "PUT":
      data = QueryDict(request.body)
      contact.firstName = data.get('firstName', contact.firstName)
      contact.lastName = data.get('lastName', contact.lastName)
      contact.phone = data.get('phone', contact.phone)
      contact.email = data.get('email', contact.email)
      contact.save()
      return JsonResponse(contact.to_json(), status=201)
    elif request.method == "DELETE":
      contact.delete()
      return JsonResponse(contact.to_json(), status=201)