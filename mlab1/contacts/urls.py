from django.urls import path
from . import views

urlpatterns = [
	path('', views.index2, name="index2"),
	path('cdetails/<int:contact_id>', views.contact_detail, name="contact_detail"),
	path('cdetails/<int:contact_id>/edit', views.contact_edit, name="contact_edit"),
	path('deleteContact/<int:contact_id>', views.contact_delete, name="contact_delete"),
	path('addContact/', views.contact_add, name="contact_add"),
]