from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models import Avg
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
    
    def delete_project(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(project_title__icontains=title).all()

    @classmethod
    def all_projects(cls):
        return cls.objects.all()

    def save_post(self):
        self.save()
    
RATE_CHOICES =[
     (1, '1 - Trash'),
     (2, '2 - Horrible'),
     (3, '3 - Terrible'),
     (4, '4 - Bad'),
     (5, '5 - Ok'),
     (6, '6 - Satisfactory'),
     (7, '7 - Good'),
     (8, '8 - Amazing'),
     (9, '9 - Perfect'),
     (10, '10 - Master Piece')
 ]
    
class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Projects,on_delete=models.CASCADE)
    body = models.TextField()
    rate_design = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    rate_content = models.PositiveSmallIntegerField(choices=RATE_CHOICES,default=0)
    rate_usability = models.PositiveSmallIntegerField(choices=RATE_CHOICES,default=0)
    
    @classmethod
    def get_ratings(cls, id):
        ratings = Review.objects.filter(project_id=id).all()
        return ratings

    def average_rating(self):
        return '{:.1f}'.format((self.rate_design + self.rate_usability + self.rate_content)/3)
        