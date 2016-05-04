from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_tag, name='index'),
    url(r'^(.*)/$', views.show_tag, name='show_tag'),
    url(r'^(.*)/prev/$', views.show_tag_prev, name='show_tag_prev'),
    url(r'^(.*)/prev/$', views.show_tag_next, name='show_tag_next'),
    url(r'^find/$', views.find_tag, name='find_tag'),
]
