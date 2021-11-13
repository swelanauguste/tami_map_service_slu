from django.db import models
from django.contrib.auth.models import AbstractUser

# from django.urls import reverse
# from django.utils.text import slugify


class User(AbstractUser):
    is_customer = models.BooleanField(default=True)
    is_dispatcher = models.BooleanField(default=False)
    is_team_lead = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    # email = models.EmailField("email address", unique=True)


# class Profile(models.Model):
#     """
#     User Profile model
#     """
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     dob = models.DateField("date of birth", blank=True, null=True)
#     gender = models.CharField(max_length=1)

#     def get_email(self):
#         return self.user.email

#     def __str__(self):
#         return self.user.username
