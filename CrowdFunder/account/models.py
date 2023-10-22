from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=11,blank=True)
    picture = models.ImageField(upload_to="account/images", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    birthdate = models.DateField(null=True,blank=True)
    profile = models.URLField(null=True,blank=True)
    country = CountryField(default='EG') 

    def get_profile_picture(self):
        if self.picture:
            return self.picture.url
        return "/media/account/images/annon.png"
    
    def __str__(self) -> str:
        return self.username
    
    def fullname(self):
        return self.first_name + " " + self.last_name