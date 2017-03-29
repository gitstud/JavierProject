from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



# Create your models here.
class SubManager(models.Manager):
	#form part 1 : name, email, passwords, bcrypt
	def validateA(self, name, email, password, cpassword, request):
		try:
			check = SubCompany.objects.get(email=email)
			messages.warning(request, 'This email is already registered.')
			return false

		except:
		
			if len(name) < 1:
				messages.warning(request, 'Company Name Required.')
				return False
				
			if not EMAIL_REGEX.match(email):
				messages.warning(request, 'Invalid Email.')
				return False

			if len(password) < 8:
				messages.warning(request, 'Your password must contain at least 8 characters.')
				return False

			if password != cpassword:
				messages.warning(request, 'Your passwords do not match')
				return False

			password = password.encode()
			hashed = bcrypt.hashpw(password, bcrypt.gensalt())

			a = SubCompany(name=name, email=email, password = hashed)
			a.save()
			return a

	#form part 2 carrier contact information
	def validateB(self, id, fname, lname, phone, stradd, city, state, zipcode, request):
		
		if len(fname) < 1:
			messages.warning(request, 'First Name Required')
			return False
		if len(fname) > 0:
			if not fname.isalpha():
				messages.warning(request, 'First Name may only include alphabet characters.')
				return False
		if len(lname) < 1:
			messages.warning(request, 'Last Name Required')
			return False
		if len(lname) > 0:
			if not lname.isalpha():
				messages.warning(request, 'Last Name may only include alphabet characters.')
				return False
		if len(stradd) < 1:
			messages.warning(request, 'Street Address Required.')
			return False
		if len(state) < 1:
			messages.warning(request, 'State Required.')
			return False
		if len(zipcode) < 1:
			messages.warning(request, 'Zipcode Required.')
			return False

		a = SubCompany.objects.get(id=id)
		a.contact_fname = fname
		a.contact_lname = lname
		a.phone = phone
		a.street_address = stradd
		a.city = city
		a.state = state
		a.zipcode = zipcode
		a.save()
		return a

	# form part 3 Shippin Fee information
	def validateC(self, id, ftime, scharge, estop, fcharge, sdry, scold, zipcodes, request):
		#going to be the banking validation function
		count = 0
		ziplist = []
		z = ''
		for i in zipcodes:
			if i.isdigit():
				z+=i
				count+=1
			if count == 5:
				ziplist.append(z)
				count = 0
				z = ''

		print(ziplist)

		ftime = float(ftime)
		scharge = float(scharge)
		estop = float(estop)
		fcharge = float(fcharge)
		sdry = float(sdry)
		scold = float(scold)
		ftime = float(ftime)

		a = SubCompany.objects.get(id=id)


		a.free_time = ftime
		a.stop_charges = scharge
		a.exam_stop = estop
		a.fuel_surcharge = fcharge
		a.storage_dry = sdry
		a.storage_cold = scold
		a.save()
		for item in ziplist:
			try:
				check = Zips.objects.get(zipcode=item)
				a.zip_service.add(check)
			except:
				check = Zips.objects.get(zipcode=item)
				b = Zips(zipcode=item)
				b.save()
				a.zip_service.add(b)
			a.save()


		return a

	#form part 4 banking information /skipping for now/
	def validateD(self, ftime, scharge, estop, fcharge, sdry, scold, request):

		return






class User(models.Model):
	admin_email = models.CharField(max_length=50)
	password = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Zips(models.Model):
	zipcode = models.CharField(max_length=30, null=True, blank=True, unique=True)
	

class SubCompany(models.Model):
	name = models.CharField(max_length=60)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=200)
	phone = models.CharField(max_length = 20)
	location = models.CharField(max_length = 200)
	free_time = models.FloatField(null=True, blank=True, default=0.00)
	stop_charges = models.FloatField(null = True, blank = True, default = 0.00)
	exam_stop = models.FloatField(null = True, blank = True, default = 0.00)
	fuel_surcharge = models.FloatField(null = True, blank = True, default = 0.00)
	storage_dry = models.FloatField(null = True, blank = True, default = 0.00)
	storage_cold = models.FloatField(null = True, blank = True, default = 0.00)
	zip_service = models.ManyToManyField(Zips)
	drayage = models.FloatField(null=True, blank=True, default=0.00)
	contact_fname = models.CharField(max_length=40, default='', null=True)
	contact_lname = models.CharField(max_length=60, default='', null=True)
	street_address = models.CharField(max_length=200, null=True)
	state = models.CharField(max_length=40, null=True)
	zipcode = models.CharField(max_length=30, null=True)
	city = models.CharField(max_length=100, null=True)
	objects = SubManager()



















