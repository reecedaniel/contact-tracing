from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models.signals import post_save
from django.dispatch import receiver


class MyUserManager(BaseUserManager):
    def create_user(self, email, company_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            company_name=company_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, company_name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            company_name=company_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    company_name = models.CharField(max_length=264,unique=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['company_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin




# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .manager import CustomUserManager
# # Create your models here.
#
# class User(AbstractUser):
#     """auth/login-related fields"""
#     username = None
#     email = models.EmailField(_('email address'), unique=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = CustomUserManager()
#
#     def __str__(self):
#         return self.email
#
#
class Profile(models.Model):
    """non-auth-related/cosmetic fields"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    max_locations = models.PositiveIntegerField(default=1)
    # Examples:
    # Display Name
    # Bios, descriptions, taglines
    # Theme (light or dark)
    # email (if not used to log in)

"""receivers to add a Profile for newly created users"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
     if created:
         Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
     instance.profile.save()
