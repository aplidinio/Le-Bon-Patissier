from django.shortcuts import render
from .models import LoginForm

# Create your views here.
def login(request):
	context ={}
	context['form']= LoginForm()
	return render(request, "WebProject/login.html", context)
