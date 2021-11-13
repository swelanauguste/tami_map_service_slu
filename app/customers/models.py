from django.db import models

from django.conf import settings

User = settings.AUTH_USER_MODEL


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, null=True)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.user.email