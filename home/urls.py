from django.conf.urls import url
from . import views

app_name='home'

urlpatterns = [
    #url(r'^$', views.home, name='home'),
    url(r'^login/$', views.loginview, name='login'),
    url(r'^signup/$', views.signupview, name='signup'),
    url(r'^logout/$', views.logoutview, name='logout'),
]