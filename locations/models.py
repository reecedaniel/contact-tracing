from django.db import models
from accounts.models import User
from django.urls import reverse
# Create your models here.
class Location(models.Model):
    CITY_CHOICES=[
        ('Swakopmund','Swakopmund'),
        ('Walvis Bay','Walvis Bay'),
        ('Windhoek','Windhoek'),
        ('Other','Other'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    address = models.CharField(max_length=264)
    city = models.CharField(max_length=20,choices=CITY_CHOICES,default='Walvis Bay')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("locations:detail",kwargs={'pk':self.pk})
