"""Platzigram views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

def hello_world(request):
	return HttpResponse('Hi, server time is {now}'.format(now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))

def hi_numbers(request):
	"""
	* make debugger with:
	import pdb; pdb.set_trace()
	* with 'c' continue the app execution
	"""
	numbers = request.GET['numbers']
	return HttpResponse(str(numbers))
