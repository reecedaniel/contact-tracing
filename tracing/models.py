from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from locations.models import Location
# Create your models here.
class Visitor(models.Model):
    name = models.CharField(max_length=264,unique=False)
    cellphone = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.name

class Visit(models.Model):
    cellphone = models.ForeignKey(Visitor,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

    def __str__(self):
        return str(self.timestamp)
