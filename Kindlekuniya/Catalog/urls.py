from django.conf.urls import url
from django.contrib.sites.models import Site
from . import views

urlpatterns = [
    # /catalog/ -> catalog homepage
    url(r'^$', views.index, name = 'index'),

]
