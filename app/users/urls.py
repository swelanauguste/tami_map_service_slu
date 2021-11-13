from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('add/employee', views.EmployeeCreateView.as_view(), name='employee-create'),
]
