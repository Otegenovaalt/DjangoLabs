from django.shortcuts import render, redirect

from contacts.models import Contact 

def index2(request):
	contacts = Contact.objects.all()
	context2 = {
		'contacts': contacts
	}
	return render(request, 'index2.html', context2)

def contact_detail(request, contact_id):
	contact = Contact.objects.get(id=contact_id)
	context2 = {
		'contact': contact
	}
	return render(request, 'contact_detail.html', context2)

def contact_add(request):
	if(request.method == 'POST'):
		firstName = request.POST['firstName']
		lastName = request.POST['lastName']
		phone = request.POST['phone']
		email = request.POST['email']
		contact = Contact(firstName = firstName, lastName = lastName, phone = phone, email = email)
		
		contact.save()
		return redirect('/contacts')
	else:
		return render(request, 'contact_add.html')
		
def contact_edit(request, contact_id):
    contact = Contact.objects.get(id = contact_id)
    if request.method == "POST":
    	firstName = request.POST['firstName']
    	lastName = request.POST['lastName']
    	phone = request.POST['phone']
    	email = request.POST['email']
    	contact.firstName = firstName
    	contact.lastName = lastName
    	contact.phone = phone
    	contact.email = email
    	contact.save()
    	return redirect('index2') 
    else:
    	return render(request, 'contact_edit.html', {"contact": contact})

def contact_delete(request, contact_id):
	contact = Contact.objects.get(id = contact_id)
	contact.delete()

	return redirect('index2')



