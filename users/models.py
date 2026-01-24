from django.db import models

# Create your models here.
 
class User_profile(models.Model):
    user_name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_Picture = models.ImageField(upload_to='profile_pic', null=True)
    