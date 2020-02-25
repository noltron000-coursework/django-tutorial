import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
	def __repr__(self):
		return self.question_text

	def was_published_recently(self):
		'''
		Checks the elapsed time since the item was published.
		If it is below one, it returns true.
		'''
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

	# create fields
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	def __repr__(self):
		return self.choice_text

	# create fields
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
