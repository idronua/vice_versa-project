from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return HttpResponse(
		'''<h1>Vice Versa</h1>
		<textarea id="home" name="home" rows="4" cols="50"></textarea><br>
		<button>Reverse!</button>'''

		)

def main(request):
	return render (request, 'main.html')