from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional user fields
    # profile_pic = models.ImageField(upload_to='profile_pic',blank=True)

    def __str__(self):
        return self.user.username

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
