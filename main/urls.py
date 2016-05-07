from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_tag, name='index'),
    url(r'^(.*)/prev/$', views.show_tag_prev, name='show_tag_prev'),
    url(r'^(.*)/next/$', views.show_tag, name='show_tag_next'),
    url(r'^(.*)/$', views.show_tag, name='show_tag'),
]
