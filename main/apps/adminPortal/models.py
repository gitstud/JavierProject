from __future__ import unicode_literals

from django.db import models



# Create your models here.
class User(models.Model):
	admin_email = models.CharField(max_length=50)
	password = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Zips(models.Model):
	zipcode = models.CharField(max_length=30, null=True, blank=True)

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
















