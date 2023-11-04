from django.db import models
from django.utils import timezone
from account.models import User
from django.contrib.postgres.fields import ArrayField
  
                           
class Project(models.Model):
    title = models.CharField(max_length=100,unique=True)
    details = models.TextField()
    total_target = models.DecimalField(decimal_places=1,max_digits=10)
    start_time = models.DateField(default=timezone.now)
    end_time = models.DateField(default=timezone.now)
    category = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='projects')
    tags = models.CharField(max_length=64,blank=True,default="")
    is_featured=models.BooleanField(default=False,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    

    @property
    def tags_array(self):
        return self.tags.strip("{}").split(',')
    
    @property
    def all_photos(self):
        return [x.photo.url for x in self.photos.all()]
    
    @property
    def thumbnail(self):
        try:
            return self.all_photos[0]
        except:
            return "/media/projects/images/project.jpg"
    
    @property
    def raised_money(self):
        return sum(list(map(lambda x: x.amount,self.donations.all())))
    
    @property
    def expired(self):
        return self.end_time < timezone.now().date()
    
    @property   
    def percentage(self):
        return 100 * float(self.raised_money) // float(self.total_target)
    
    @property
    def remaining_time(self):
        return (self.end_time - timezone.now().date()).days

    @property
    def rate(self):
        reviews = self.reviews.all()
        if len(reviews):
            return round(sum(list(map(lambda x: x.rate,reviews)))/len(reviews),1)
        return 0
    
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

class Donation(models.Model):
    amount = models.FloatField()
    project = models.ForeignKey(Project , on_delete=models.CASCADE , related_name='donations')
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='donations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)

class Photo(models.Model):
    photo = models.ImageField(upload_to="projects/images/%Y/%m/%d/%H/%M/%S/", null=True, blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE, related_name='photos')


    