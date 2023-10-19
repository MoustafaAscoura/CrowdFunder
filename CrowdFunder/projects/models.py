from django.db import models
from django.utils import timezone
from account.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    total_target = models.FloatField()
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    rate = models.IntegerField(default=0)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name='category')
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='owner')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Donation(models.Model):
    donation = models.FloatField()
    project = models.ForeignKey(Project , on_delete=models.CASCADE , related_name='donation_project')
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='donation_user')
    created_at = models.DateTimeField(auto_now_add=True)

