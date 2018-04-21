from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name="index"),
	path('add/', views.add, name="add"),	
	path('complete/<int:todo_id>', views.completeTodo, name='complete'),
	path('details/<int:todo_id>', views.todo_detail, name="todo_detail"),
	path('delete/<int:todo_id>', views.deleteTodo, name='delete'),
	path('edit/<int:todo_id>', views.editTodo, name='editTodo'),
	path('sortByDate/', views.sortByDate, name='sortByDate'),
	path('sortByName/', views.sortByName, name='sortByName'),
	path('completedList/', views.completedList, name='completedList'),
	path('sortByPriority/', views.sortByPriority, name='sortByPriority'),
]
