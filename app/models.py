from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Profile(models.Model):
    profile_photo = CloudinaryField('profilePhoto')
    bio = models.TextField(blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    github = models.CharField(max_length=255,blank=True,null=True)
    instagram = models.CharField(max_length=255,blank=True,null=True)
    linkedin = models.CharField(max_length=255,blank=True,null=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
class Projects(models.Model):
    project = CloudinaryField('project')
    project_title= models.TextField()
    project_description= models.TextField()
    site_link = models.CharField(max_length=60)
    score = models.IntegerField(default=0,validators=[MaxValueValidator(5),MinValueValidator(0)])
    user= models.ForeignKey(Profile,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return str(self.pk)