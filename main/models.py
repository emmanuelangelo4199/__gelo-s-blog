from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    mission = models.TextField()
    vision = models.TextField()
    description = models.TextField()
    logo = models.ImageField(upload_to='about_us/logos/')
    
    def __str__(self):
        return self.title
    

class ContactInfo(models.Model):
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    linkedln = models.URLField(blank=True, null=True)
    x = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.email
    

class siteSettings(models.Model):
    site_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='site_settings/logos/')
    favicon = models.ImageField(upload_to='site_settings/favicon/')
    
    def __str__(self):
        return self.site_name