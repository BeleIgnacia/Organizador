from django.shortcuts import render

def index_inicio(request):
	return render(request,'inicio.html')