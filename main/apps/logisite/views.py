from django.shortcuts import render, redirect
from models import User

# Create your views here.
def index(request):
	return render(request, 'logisite/index.html')

def portal(request):
	return render(request, 'logisite/account.html')

def validateAdmin(request):
	return redirect('main:index')