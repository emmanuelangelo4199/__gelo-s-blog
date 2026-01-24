from django.db import models
from posts.models import Articles

# Create your models here.

class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='comments')
    user_name = models.CharField(max_length=100)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comented by {self.user_name} on {self.article.headline}"