from django.urls import re_path
from countries import views

urlpatterns = [
        re_path(r'^api/countries$', views.countries_list),
        re_path(r'^api/countries/(?P<pk>[0-9]+)$', views.countries_details)
]
