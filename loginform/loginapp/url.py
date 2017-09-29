from django.conf.urls import url
from.import views
urlpatterns=[
			url(r'^form/',views.fromview,name='form'),
			url(r'^login/',views.login,name='login'),
			url(r'^logout/',views.logout,name='logout'),
			]