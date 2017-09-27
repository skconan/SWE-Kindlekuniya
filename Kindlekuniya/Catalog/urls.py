from django.conf.urls import url
from . import views

urlpatterns = [
    # /catalog/ -> catalog homepage
    url(r'^$', views.index, name = 'index'),

]
