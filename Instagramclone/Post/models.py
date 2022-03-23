from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Posts(models.Model):
    id = models.UUIDField(primary_key=True)
    post = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=100)
    created_by = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    def __str__(self):
        return self.text
        
class Comment(models.Model):
    comment = models.CharField(max_length=250)
    comment_by = models.ForeignKey(User,related_name='comment',on_delete=models.CASCADE)
    comment_on = models.ForeignKey(Posts,related_name='comment',on_delete=models.CASCADE)
    comment_at = models.DateTimeField(auto_now_add=True)
    