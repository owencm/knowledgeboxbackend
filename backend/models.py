from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=20)
	def __unicode__(self):
		return self.username

class QaItem(models.Model):
	question = models.CharField(max_length=400)
	answer = models.CharField(max_length=400)
	url = models.CharField(max_length=400)
	creator = models.ForeignKey(User)
	created_at = models.DateTimeField('date published')
	def __unicode__(self):
		return self.question