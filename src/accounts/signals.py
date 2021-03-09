from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings
# from .models import Person
# from .models import Profile

# @receiver(post_save, sender=User)
# def post_save_profile_create(sender, instance, created, **kwargs):
#     if created:
#         pass
#         # Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def post_save_receiver(sender, instance, created, **kwargs):
#     if created:
#         Person.objects.create(user=instance)


# post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)
