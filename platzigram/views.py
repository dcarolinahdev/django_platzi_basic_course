"""Platzigram views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

def hello_world(request):
	now = datetime.now()
	return HttpResponse('Hi, server time is {now}'.format(now=str(now)))