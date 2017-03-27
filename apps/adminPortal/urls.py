from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login$', views.portal, name='admin_portal'),
	url(r'^register_a$', views.RegisterA, name='registerA'),
	url(r'^register/contact/info/(?P<company>\d+)/$', views.RegisterB, name='registerB'),
	url(r'^register/shipping/info/(?P<company>\d+)/$', views.RegisterC, name='registerC'),
	url(r'^register/banking/info/(?P<company>\d+)/$', views.RegisterD, name='registerD'),
	url(r'^admin_validate$', views.validateAdmin, name='admin_validate'),
	url(r'^business_dashboard$', views.b_dash, name='b_dash'),
]