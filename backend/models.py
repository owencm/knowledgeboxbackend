from django.db import models
import datetime
from django.utils.timezone import utc

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=40)

	def __unicode__(self):
		return self.username

class QaItem(models.Model):
	question = models.CharField(max_length=400)
	answer = models.CharField(max_length=400)
	url = models.CharField(max_length=400)
	creator = models.ForeignKey(User, related_name='owner')
	created_at = models.DateTimeField('date published')
	learners = models.ManyToManyField(User)
	def __unicode__(self):
		return self.question

class QResponse(models.Model):
	qid = models.ForeignKey(QaItem, related_name='qaitem')
	userid = models.ForeignKey(User, related_name='user')
	correct = models.BooleanField()
	answered_at = models.DateTimeField('date answered')

# class Learning(models.Model):
# 	qaitem = models.ForeignKey(QaItem)
# 	user = models.ForeignKey(User)