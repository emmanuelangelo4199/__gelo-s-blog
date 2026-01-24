from django.db import models

# Create your models here.

class Reporter(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='reporter/profile_pic/')
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name 


class Categories(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    

class Articles(models.Model):
    headline = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey("Reporter", on_delete=models.CASCADE)
    category = models.ForeignKey("Categories", on_delete=models.CASCADE)
    featured_Image = models.ImageField(upload_to='articles/featured_images/', blank=True, null=True)
    
    def __str__(self):
        return self.headline
    
    
class Image(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='article/images/')
    
    def __str__(self):
        return f"Image for {self.article.headline}"
    
    
class Video(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='videos')
    video_url = models.URLField()
    
    def __str__(self):
        return f"Video for {self.article.headline}"
    
    




