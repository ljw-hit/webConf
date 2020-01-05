from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'webconf', views.getIndex, name='webconf'),
    url(r'ip',views.ipMess,name='ip'),
    url(r'startProxy',views.startproxy,name='startProxy'),
    url(r'delay',views.delayTime,name='delay'),
]