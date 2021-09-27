from django.shortcuts import render, redirect

def index_view(response):
	return render(response, 'clearinghouse/index.html')



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