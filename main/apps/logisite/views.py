from django.shortcuts import render, redirect
from models import User

# Create your views here.
def index(request):
	return render(request, 'logisite/index.html')

def portal(request):
	return render(request, 'logisite/account.html')

def validateAdmin(request):
	print(request.POST['userEmail'])
	try:
		a = User.objects.get(admin_email=request.POST['userEmail'])
	except:
		return redirect('main:index')
	if a.password == request.POST['userPassword']:
		print('******************')
	else:
		print('################')
	return redirect('main:b_dash')

def b_dash(request):
	return render(request, 'logisite/businessDashboard.html')