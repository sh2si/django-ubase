from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Username', on_delete=models.CASCADE)
    nationalID = models.CharField('National Code', max_length=10)
    phone = models.CharField('Phone Number', max_length=14)

    def __str__(self):
        return '%s (%s)' % (self.phone, self.user)
