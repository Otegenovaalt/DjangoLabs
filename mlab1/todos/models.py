from django.db import models
from datetime import datetime

# Create your models here.
class Todo(models.Model):
	title = models.CharField(max_length=200)
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	complete = models.BooleanField(default=False)
	priority = models.CharField(default='1', max_length=5)

	def __str__(self):
		return self.title