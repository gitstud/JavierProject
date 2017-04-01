from django.shortcuts import render, redirect, reverse

from ..adminPortal.models import SubCompany

# Create your views here.
def Dash(request, company):
	company = SubCompany.objects.get(id=company)
	return render(request, 'carrier/carrierDash.html', {'company':company})
