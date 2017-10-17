"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_view

from member.views import signup
from post.views import post_list, post_create, post_detail, comment_create

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', 'base.html'),
    url(r'^post/$', post_list, name='post_list'),
    url(r'^post/create/$', post_create, name='post_create'),
    url(r'^post/(?P<post_pk>\d+)$', post_detail, name='post_detail'),
    url(r'^post/(?P<post_pk>\d+)/comment/$', comment_create, name='comment_create'),
    url(r'^member/signup/$', signup, name='signup'),
    url(r'^member/login/$', auth_view.login, {'template_name': 'member/login.html'}, name='login'),
    url(r'^member/logout/$', auth_view.logout, {'next_page':'login'}, name='logout'),
]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
