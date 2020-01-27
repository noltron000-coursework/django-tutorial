from django.db import models

class Question(models.Model):
	def __repr__(self):
		return self.question_text

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
