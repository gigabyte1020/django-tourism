
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('holidays', views.holidays),
    path('sgt', views.sgt),
    path('guide', views.guides),

    path('boo', views.boo),
    path('logout', views.logout_r),
]