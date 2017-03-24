from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^admin_portal', views.portal, name='admin_portal'),
	url(r'^admin_login', views.validateAdmin, name='admin_validate'),
]