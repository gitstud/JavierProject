from django.shortcuts import render, redirect
from models import User

# Create your views here.
def portal(request):
	return render(request, 'adminPortal/account.html')

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
	return redirect('account:b_dash')

def b_dash(request):
	return render(request, 'adminPortal/businessDashboard.html')
