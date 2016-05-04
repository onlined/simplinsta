from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([a-zA-Z0-9]*)/$', views.show_tag, name='show_tag'),
    url(r'^([a-zA-Z0-9]*)/([0-9]*)/$', views.show_tag, name='show_tag_page'),
    url(r'^find/$', views.find_tag, name='find_tag'),
]
