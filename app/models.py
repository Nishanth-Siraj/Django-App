from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        
        verbose_name = 'Post Table'
        verbose_name_plural = 'Posts Table'
        ordering = [('title').lower()]

class Tags(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='tags')
    tag = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tag 
    
    class Meta:
        ordering = ['-id']
        
        verbose_name = 'Tag Table'
        verbose_name_plural = 'Tags Table'