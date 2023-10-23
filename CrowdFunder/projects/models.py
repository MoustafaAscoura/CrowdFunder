from django.db import models
from django.utils import timezone
from account.models import User
from django.contrib.postgres.fields import ArrayField
  
                           
class Project(models.Model):
    title = models.CharField(max_length=100,unique=True)
    details = models.TextField()
    total_target = models.DecimalField(decimal_places=3,max_digits=10)
    start_time = models.DateField(default=timezone.now)
    end_time = models.DateField(default=timezone.now)
    category = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='owner')
    tags = ArrayField(models.CharField(max_length=64),blank=True,default=[])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Donation(models.Model):
    amount = models.FloatField()
    project = models.ForeignKey(Project , on_delete=models.CASCADE , related_name='donation_project')
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='donation_user')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)

