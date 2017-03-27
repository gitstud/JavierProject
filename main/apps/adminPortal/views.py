from django.shortcuts import render, redirect
from models import User, SubCompany
from pprint import pprint

# Create your views here.
def portal(request):
	return render(request, 'adminPortal/cAccount.html')

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

def cRegister(request):
	print(request.POST['cname'])
	print(request.POST['cemail'])
	print(request.POST['cpass'])
	print(request.POST['ccpass'])
	print(request.POST['ctype'])
	company = SubCompany(name=request.POST['cname'], email=request.POST['cemail'], password=request.POST['cpass'])
	company.save()
	return redirect('account:b_dash')
