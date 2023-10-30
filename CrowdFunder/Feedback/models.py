from django.db import models
from projects.models import Project 
from account.models import User


class Comment(models.Model):
    content=models.CharField(max_length=500)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='comments')
    user =models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    review=models.CharField(max_length=500)
    rate = models.DecimalField(max_digits=2,decimal_places=1)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='reviews')
    user =models.ForeignKey(User,on_delete=models.CASCADE,related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def rates(self): #This transforms the rates number to list of 0,0.5,1 to convert it later to stars
        rates_list = []
        rate = self.rate

        for i in range(1,6):
            if i - rate >= 1:
                rates_list.append(0)
            elif i - rate > 0.2:
                rates_list.append(0.5)
            else:
                rates_list.append(1)
        
        return rates_list
    
class Report(models.Model):
    reason=models.CharField(max_length=500)
    status=models.CharField(max_length=15)
    project = models.ForeignKey(Project,on_delete=models.CASCADE, related_name='reports', null=True)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE, related_name='reports', null=True)
    user =models.ForeignKey(User,on_delete=models.CASCADE, related_name='reports')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.reason    


    
class Reply(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='replies')
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE, related_name='replies')
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

