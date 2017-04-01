from django.shortcuts import render, redirect, reverse, HttpResponse
from models import User, SubCompany, Zips
import json

# Create your views here.
def portal(request):
	return render(request, 'adminPortal/registerA.html')

def fportal(request):
	return render(request, 'adminPortal/fregisterA.html')

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

# login or register page
def RegisterA(request):
	company = SubCompany.objects.validateA(name=request.POST['cname'], email=request.POST['cemail'], password=request.POST['cpass'], cpassword=request.POST['ccpass'], request=request)
	print('$$$$$$$$$$$', company)
	if company == False:
		return redirect('account:admin_portal')
	else:
		return redirect(reverse('account:registerB', args=(company.id,)))

# company information page
def RegisterB(request, company):
	a = SubCompany.objects.get(id=company)
	context = {'company':a.name, 'id':a.id}
	return render(request, 'adminPortal/registerB.html', context)

# shipping information page
def RegisterC(request, company):
	x = request.POST
	vComp = SubCompany.objects.validateB(id=company, fname=x['first_name'], lname=x['last_name'], phone=x['phone'], stradd=x['address'], city=x['city'], state=x['state'], zipcode=x['zip'], request=request)
	if vComp == False:
		a = SubCompany.objects.get(id=company)
		return redirect(reverse('account:registerB', args=(a.id,)))
	else:
		context = {'company':vComp.name, 'id':vComp.id}
		return render(request, 'adminPortal/registerC.html', context)

# bank accounts /skip for now/
def RegisterD(request, company):
	print('$$$$$$$',request.POST['zip'])
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
	
	return redirect(reverse('account:registerC', args=(company.id,)))

def RegisterReview(request, company):
	print(request.POST['zip'])
	x = request.POST

	a = SubCompany.objects.validateC(id=company,ftime=x['free_time'],scharge=x['stop_charges'],estop=x['exam_stop'],fcharge=x['fuel_surcharge'],sdry=x['storage_dry'],scold=x['storage_cold'],zipcodes=x['zip'],request=request)

	# if we need to go back run this
	# return redirect(reverse('account:registerC', args=(a.id,)))
	return render(request, 'adminPortal/registerReview.html', {'company':a})













