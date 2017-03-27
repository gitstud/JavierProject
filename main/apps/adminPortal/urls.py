from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^admin_portal', views.portal, name='admin_portal'),
	url(r'^register_customer', views.cRegister, name='register'),
	url(r'^admin_validate', views.validateAdmin, name='admin_validate'),
	url(r'^business_dashboard', views.b_dash, name='b_dash'),
]