from django.db import models

# Create your models here.

class blog(models.Model):
	name = models.CharField(max_length=30, unique=True)
	content = models.TextField(max_length=4000, unique=True)

	def __str__(self):
		return self.name