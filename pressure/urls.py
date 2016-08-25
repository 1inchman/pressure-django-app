from django.confs.urls import url
from pressure import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
