from django.conf.urls import url 
from . import views 
from django.contrib.auth.views import login, logout

urlpatterns = [
	url(r'^$', views.home), # conecta con la funcion home del archivo views
	url(r'^login/$', login,{'template_name':'acounts/login.html'}), # conecta con la funcion home del archivo views
	url(r'^logout/$', logout,{'template_name':'acounts/logout.html'}), # conecta con la funcion home del archivo views

]