from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_tag, name='index'),
    url(r'^(.*)/next/$', views.show_tag, name='show_tag_next'),
    url(r'^(.*)/$', views.show_tag, name='show_tag'),
]
