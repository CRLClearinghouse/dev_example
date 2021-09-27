from django.shortcuts import render, redirect
from .models import *

def index_view(response):
	num_people = Person.objects.all().count()
	num_courts = Court.objects.all().count()
	try:
		num_people_courts = PersonCourt.objects.all().count()
	except:
		num_people_courts = 0
	return render(response, 'clearinghouse/index.html', {
		'num_people': num_people,
		'num_courts': num_courts,
		'num_people_courts': num_people_courts,
	})



"""
Developer can ignore these
"""
def setup_view(response):
	from .hidden_code import setup_project
	setup_project()
	try:
		from .hidden_code import setup_project
		#setup_project()
	except ImportError:
		print('hidden_code not available')
	return render(response, 'clearinghouse/index.html')

def import_view(response):
	from .hidden_code import import_data
	import_data()
	try:
		from .hidden_code import import_data
		#import_data()
	except ImportError:
		print('hidden_code not available')
	return render(response, 'clearinghouse/index.html')