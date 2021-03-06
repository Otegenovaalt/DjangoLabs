from django.urls import path
from . import views

urlpatterns = [
	path('', views.todo_list),
	path('complete', views.todo_complete),
	path('sortByPriority', views.todo_priority),
	path('detail/<int:todo_id>', views.todo_detail),
]