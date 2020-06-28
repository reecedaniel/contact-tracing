from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from locations.models import Location
from django.db.models import Min, Max, Sum
# Create your models here.
class Visitor(models.Model):
    name = models.CharField(max_length=264,unique=False)
    cellphone = models.CharField(max_length=10,unique=True)
    visitor_email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name



class Visit(models.Model):
    cellphone = models.ForeignKey(Visitor,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=3,decimal_places=1)
    dry_cough = models.BooleanField(default=False)
    breathing = models.BooleanField(default=False)
    flu=models.BooleanField(default=False)
    other_contact=models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

    def __str__(self):
        return str(self.timestamp)
