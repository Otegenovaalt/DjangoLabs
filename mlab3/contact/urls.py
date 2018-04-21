from django.urls import path, include

from contact import views


urlpatterns = [
	path('', views.contact_list),
	path('detail/<int:contact_id>', views.contact_detail),
]