from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(unique=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        email_username = self.email.split('@')[0]
        if not self.username:
            self.username = email_username
        super(User, self).save(*args, **kwargs) 




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True,)


    def __str__(self):
        return self.user.username    


    def save(self, *args, **kwargs):
        email_username, _ = self.user.email.split('@')
        if not self.full_name:
            self.full_name = self.user.username
        super(Profile, self).save(*args, **kwargs)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
