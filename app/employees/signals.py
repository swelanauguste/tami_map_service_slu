from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Employee
from customers.models import Customer

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    if instance.is_customer == False:
        Employee.objects.get_or_create(user=instance)
        # Customer.objects.delete(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_customer == False:
        instance.employee.save()
        # instance.customer.delete()
