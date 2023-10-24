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
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='projects')
    photo = models.ImageField(upload_to="projects/images/%Y/%m/%d/%H/%M/%S/", null=True, blank=True)
    tags = ArrayField(models.CharField(max_length=64),blank=True,default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    @property
    def thumbnail(self):
        return self.photo.url if self.photo else "/media/projects/images/project.jpg"
    
    @property
    def raised_money(self):
        return sum(list(map(lambda x: x.amount,self.donations.all())))
    
    @property
    def expired(self):
        return self.end_time < timezone.now().date()



class Donation(models.Model):
    amount = models.FloatField()
    project = models.ForeignKey(Project , on_delete=models.CASCADE , related_name='donations')
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='donations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)

