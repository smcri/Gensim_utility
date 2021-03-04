from django.db import models

# Create your models here.

class blog(models.Model):
	name = models.CharField(max_length=30, unique=True)
	content = models.TextField(max_length=4000, unique=True)
	description = models.TextField(max_length=200000)
	written_by = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class datasets(models.Model):
	name = models.CharField(max_length=30, unique=True)
	path = models.CharField(max_length=30, unique=True)
	description = models.TextField(max_length=4000, unique=True)

	def __str__(self):
		return self.name
