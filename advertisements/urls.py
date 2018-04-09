from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^index/', views.index, name="index"),
    url(r'^home/', views.home, name="home"),
    url(r'^contact/', views.contact, name="contact"),
    url(r'^login/', views.login, name="login"),
    url(r'^register/', views.register, name="register"),
    url(r'^logout/', views.logout, name="logout"),
    url(r'^checkuser/', views.checkuser, name="checkuser"),
    url(r'^post/', views.post, name="post"),
    url(r'^deletepost/', views.deletepost, name="deletepost"),
    url(r'^addpost/', views.addpost, name="addpost"),
    url(r'^updatepost/(?P<post_id>\d+)/$', views.updatepost, name="updatepost"),
    url(r'^viewpost/(?P<post_id>\d+)/$', views.viewpost, name="viewpost"),
    url(r'^search/$', views.search, name="search"),
    url(r'^update/', views.update, name="update"),
    url(r'^profile/', views.profile, name="profile"),
    url(r'^searchjob/', views.searchjob, name="searchjob"),
    url(r'^getpost/(?P<post_id>\d+)/$', views.getpost, name="getpost")
]