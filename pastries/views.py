from django.shortcuts import render
from django.shortcuts import render_to_response



def home_page(request):
	'Display map'
	return render_to_response('home.html', {

		})