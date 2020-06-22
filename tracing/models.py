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
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

    cellphone = models.ForeignKey(Visitor,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=3,decimal_places=1,default=36.5)
    dry_cough = models.BooleanField(choices=BOOL_CHOICES,default=False)
    breathing = models.BooleanField(choices=BOOL_CHOICES,default=False)
    flu=models.BooleanField(choices=BOOL_CHOICES,default=False)
    other_contact=models.BooleanField(choices=BOOL_CHOICES,default=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

    def __str__(self):
        return str(self.timestamp)
