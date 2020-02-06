### `django-admin startproject`

Dev Server: 
1. `python ./manage.py runserver`
	- Specify port: `python ./manage.py runserver 8080`
	- Public wifi: `python ./manage.py runserver 0:8000`
2. try out the `python manage.py shell` command
	- Start with: `from polls.models import Choice, Question`
	- `Question.objects.all()`
	- `Question.objects.filter(id=1)`

Tutorial Source:
- https://docs.djangoproject.com/en/2.2/intro
