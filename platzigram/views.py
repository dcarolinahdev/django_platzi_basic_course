"""Platzigram views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

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

def sort_integers(request):
	"""Return a JSON response with sorted integers."""
	numbers = [int(i) for i in request.GET['numbers'].split(',')]
	sorted_ints = sorted(numbers)
	data = {
		'status': 'ok',
		'numbers': sorted_ints,
		'message': 'Integers sorted successfully.'
	}
	return HttpResponse(
		json.dumps(data, indent=4),
		content_type='application/json'
	)

def say_hi(request, name, age):
	"""Return a greeting."""
	if age < 12:
		message = 'Sorry {}, you are not allowed here'.format(name)
	else:
		message = 'Hello, {}! Welcome to Platzigram'.format(name)
	return HttpResponse(message)
