from django.conf.urls import url
from . import views

urlpatterns = [
	#carrier register/login
	url(r'^login$', views.portal, name='admin_portal'),
	#admin login for full site stats
	url(r'^register_a$', views.RegisterA, name='registerA'),
	#carrier contact info
	url(r'^register/contact/info/(?P<company>\d+)/$', views.RegisterB, name='registerB'),
	#carrier shipping info
	url(r'^register/shipping/info/(?P<company>\d+)/$', views.RegisterC, name='registerC'),
	#carrier banking info /skip for now/
	url(r'^register/banking/info/(?P<company>\d+)/$', views.RegisterD, name='registerD'),
	#carrier registration review
	url(r'register/review/(?P<company>\d+)/$', views.RegisterReview, name='registerReview'),
	url(r'^admin_validate$', views.validateAdmin, name='admin_validate'),
	#forward register/login
	url(r'^login$', views.fportal, name='fadmin_portal'),
]