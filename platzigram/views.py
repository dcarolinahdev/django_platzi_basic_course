"""Platzigram views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

def hello_world(request):
	return HttpResponse('Hi, server time is {now}'.format(now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))
