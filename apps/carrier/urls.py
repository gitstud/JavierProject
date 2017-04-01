from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^business_dashboard/(?P<company>\d+)/$', views.Dash, name='dash'),
]