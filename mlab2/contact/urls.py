from django.urls import path
from . import views

urlpatterns = [
	path('', views.contact_list),
	path('detail/<int:contact_id>', views.contact_detail)
]