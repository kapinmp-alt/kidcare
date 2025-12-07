# from .models import UserProfile
# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver

# from django.core.exceptions import ObjectDoesNotExist

# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#         instance.userprofile.save()


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     try:
#         instance.userprofile.save()
#     except ObjectDoesNotExist:
#         UserProfile.objects.create(user=instance)


# @receiver(post_save, sender=User)
