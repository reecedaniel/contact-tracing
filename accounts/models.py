from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional user fields
    # profile_pic = models.ImageField(upload_to='profile_pic',blank=True)
    max_locations = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# class Location(models.Model):
#     CITY_CHOICES=[
#         ('Swakopmund','Swakopmund'),
#         ('Walvis Bay','Walvis Bay'),
#         ('Windhoek','Windhoek'),
#         ('Other','Other'),
#     ]
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     name = models.CharField(max_length=264)
#     address = models.CharField(max_length=264)
#     city = models.CharField(max_length=20,choices=CITY_CHOICES,default='Walvis Bay')
#
#     def __str__(self):
#         return self.name
