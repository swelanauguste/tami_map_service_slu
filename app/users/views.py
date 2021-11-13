from django.shortcuts import render
from django.views.generic import CreateView

from .models import User


class EmployeeCreateView(CreateView):
    model = User
    fields = [
        "username",
        "email",
        "password",
        "is_customer",
        "is_dispatcher",
        "is_team_lead",
        "is_driver",
    ]
    # template_name = 'users/employee_form.html'
