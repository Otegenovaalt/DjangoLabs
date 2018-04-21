from django.db import models

class Todo(models.Model):
	title = models.CharField(max_length=200)
	priority = models.CharField(default='1', max_length=5)
	complete = models.BooleanField(default=False)

	def to_json(self):
		return {
			'id': self.id,
			'title': self.title,
			'priority': self.priority,
			'complete': self.complete,
		}

	def __str__(self):
		return self.title
# Create your models here.
