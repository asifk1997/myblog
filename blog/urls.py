from django.conf.urls import url
from django.urls import path
from django.conf.urls import include
from . import views

app_name='blog'

urlpatterns=[
    path('',views.index,name='index'),
    path('<int:blogpost_id>/',views.detail,name='detail'),
    path('create_blogpost/',views.create_blogpost,name='create_blogpost'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

]