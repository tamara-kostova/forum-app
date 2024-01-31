from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(null=True,blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.CASCADE,related_name="posts")
    created_at = models.DateTimeField(null=True, auto_now_add=True)

class Comment(models.Model):
    body = models.TextField(null=True,blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.CASCADE,related_name="comments")
    post = models.ForeignKey(Post,null=True, blank=True,on_delete=models.CASCADE,related_name="comments")
    created_at = models.DateTimeField(null=True, auto_now_add=True)