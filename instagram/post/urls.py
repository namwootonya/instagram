from django.conf.urls import url

from .views import post_list, post_create, post_detail, comment_create, post_delete

urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^create/$', post_create, name='post_create'),
    url(r'^(?P<post_pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^delete/(?P<post_pk>\d+)/$', post_delete, name='post_delete'),
    url(r'^(?P<post_pk>\d+)/comment/$', comment_create, name='comment_create'),
]
