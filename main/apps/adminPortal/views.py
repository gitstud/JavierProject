from django.shortcuts import render, redirect, reverse
from models import User, SubCompany
import json

# Create your views here.
def portal(request):
	return render(request, 'adminPortal/registerA.html')

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

def RegisterA(request):
	company = SubCompany(name=request.POST['cname'], email=request.POST['cemail'], password=request.POST['cpass'])
	company.save()
	return redirect(reverse('account:registerB', args=(company.id,)))

def RegisterB(request, company):
	a = SubCompany.objects.get(id=company)
	context = {'company':a}
	return render(request, 'adminPortal/registerB.html', context)

def RegisterC(request, company):
	a = SubCompany.objects.get(id=company)
	a.contact_fname = request.POST['first_name']
	a.contact_lname = request.POST['last_name']
	a.phone = request.POST['phone']
	a.street_address = request.POST['address']
	a.city = request.POST['city']
	a.state = request.POST['state']
	a.zipcode = request.POST['zip']
	a.save()
	context = {'company':a}
	return render(request, 'adminPortal/registerC.html', context)

def RegisterD(request, company):
	a = SubCompany.objects.get(id=company)
	a.free_time = float(request.POST['free_time'])
	a.stop_charges = float(request.POST['stop_charges'])
	a.exam_stop = float(request.POST['exam_stop'])
	a.fuel_surcharge = float(request.POST['fuel_surcharge'])
	a.storage_dry = float(request.POST['storage_dry'])
	a.storage_cold = float(request.POST['storage_cold'])
	a.save()
	print(a.storage_cold)
	zips = request.POST['zip'].split()
	print(zips)

	context = {'company':a}
	return render(request, 'adminPortal/registerD.html', context)













