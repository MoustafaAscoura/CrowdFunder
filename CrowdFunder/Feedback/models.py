from django.db import models
from projects.models import Project 
from account.models import User


# Create your models here.
class Comment(models.Model):
    cotent=models.CharField(max_length=500)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='comments')
    user =models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)




class Review(models.Model):
    review=models.CharField(max_length=500)
    rate = models.DecimalField(max_digits=2,decimal_places=1)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='reviews')
    user =models.ForeignKey(User,on_delete=models.CASCADE,related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)


class Report(models.Model):
    reason=models.CharField(max_length=500)
    status=models.CharField(max_length=5)
    project = models.ForeignKey(Project,on_delete=models.CASCADE, related_name='reports')
    user =models.ForeignKey(User,on_delete=models.CASCADE, related_name='reports')
    created_at = models.DateTimeField(auto_now_add=True)

