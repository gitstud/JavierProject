from django.shortcuts import render, redirect, reverse
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
	company = SubCompany(name=request.POST['cname'], email=request.POST['cemail'], password=request.POST['cpass'])
	company.save()
	return redirect(reverse('account:registerContinued', args=(company.id,)))

def cRegisterContinued(request, company):
	a = SubCompany.objects.get(id=company)
	context = {'company':a}
	return render(request, 'adminPortal/cAccountC.html', context)
