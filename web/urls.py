from django.urls import path, re_path

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^compute/(?P<field_size>[\d.]+)/(?P<age>[\d.]+)/(?P<lambda_min>[\d.]+)/(?P<lambda_max>[\d.]+)/(?P<lambda_step>[\d.]+)/', views.compute, name="compute"),
    re_path(r'^get_plot/(?P<plot>\w+)/(?P<grid>\d+)/(?P<cie31>\d+)/(?P<cie64>\d+)/(?P<labels>\d+)/(?P<norm>\d+)', views.get_plot, name='get_plot'),
    re_path(r'^get_csv/(?P<plot>\w+)', views.get_csv, name="get_csv"),
    re_path(r'^get_table/(?P<plot>\w+)/(?P<norm>\d+)', views.get_table, name="get_table"),
    re_path(r'^get_description/(?P<plot>\w+)/(?P<norm>\d+)', views.get_description, name="get_description"),
]


