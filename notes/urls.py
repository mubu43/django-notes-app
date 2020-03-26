from django.conf.urls import url
from . import views

app_name = 'notes'

urlpatterns = [
    url(r'^$', views.notes_list, name="list"),
    url(r'^add/$', views.notes_add, name="add"),
    url(r'^delete/(?P<id>[\d]+)/$', views.notes_delete, name="delete"),
    url(r'^edit/(?P<id>[\d]+)/$', views.notes_edit, name="edit"),
]