"""Library_ManageSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from LMS import views
#from .import views
#
urlpatterns = [
    url(r'^$', views.welcome_page, name='welcome_page'),
    url(r'^welcome/', views.welcome_page,name='welcome_page'),
    url(r'^login/$', views.login_page, name='login_page'),
    url(r'^login/1$', views.login_action, name='login_action'),
    url(r'^signup/$', views.signup_page, name='signup_page'),
    url(r'^signup/1$', views.signup_action, name='signup_action'),
    url(r'^logout/$', views.logout_action, name='logout_action'),
    url(r'^index/$', views.index, name='index'),
    url(r'^bookslist/$', views.bookslist,name='bookslist'),
    url(r'^record/$', views.record_page,name='record_page'),

    url(r'^record/delete(?P<record_id>[0-9]+)$', views.delete_waiting,name='delete_waiting'),
    url(r'^book/(?P<book_id>[0-9]+)$', views.book_page,name='book_page'),
    url(r'^record/borrow$', views.borrow_action,name='borrow_action'),

    url(r'^bookslist/search/$', views.search_action,name='search_action'),

    url(r'^admin/', admin.site.urls),

]
