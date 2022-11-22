from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('view_all',views.view_all, name='view_all'),
    path('add_emp',views.add_emp, name='add_emp'),
    path('rem_emp',views.rem_emp, name='rem_emp'),
    path('rem_emp/<int:emp_id>',views.rem_emp, name='rem_emp'),
    path('filter_emp',views.filter_emp, name='filter_emp'),
]
