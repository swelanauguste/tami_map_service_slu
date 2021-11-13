from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Customer
from employees.models import Employee

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.is_customer:
        if created:
            Customer.objects.get_or_create(user=instance)
        # else:
        #     Customer.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_customer:
        instance.customer.save()
        # instance.employee.delete()
