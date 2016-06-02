from django.conf.urls import url

from . import views

app_name = 'catalogue'
urlpatterns = [
    url(r'^$', views.product_group, name='group'),
    ]