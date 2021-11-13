from django.db import models
import uuid
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=10, blank=True, unique=True)
    phone = models.CharField(max_length=10, null=True)
    
    def save(self, *args, **kwargs):
        if not self.emp_id:
            self.emp_id = str(uuid.uuid4().hex[:6])
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.user.email