from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/jobs/')
    title = models.CharField(max_length=200 ,null= True)
    summary = models.CharField(max_length=5000,null= True)
   # video = models.FileField(upload_to='images/',null=True) 

    def __str__(self):
        return self.title
    
class Project(models.Model):
    image = models.ImageField(upload_to='images/projects/')
    title = models.CharField(max_length=200, null= True)
    summary = models.CharField(max_length=5000, null= True)


    def __str__(self):
        return self.title

