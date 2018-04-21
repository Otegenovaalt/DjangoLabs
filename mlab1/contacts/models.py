from django.db import models

class Contact(models.Model):
	firstName = models.CharField(max_length=100)
	lastName = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	email = models.CharField(max_length=100)

	def __str__(self):
		return self.firstName
# Create your models here.
