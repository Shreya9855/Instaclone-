from django.db import models

from User.models import UserModel


# Create your models here.
class PostModel(models.Model):
    id = models.UUIDField(primary_key=True)
    post = models.ImageField()
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserModel,related_name='posts',on_delete=models.CASCADE)
    # comment = models.ForeignKey(CommentModel,related_name='comment',on_delete=models.CASCADE)
    def __str__(self):
        return self.text
        
class CommentModel(models.Model):
    id = models.UUIDField(primary_key=True)
    comment = models.CharField(max_length=250)
    comment_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comment')
    comment_on = models.ForeignKey('PostModel',related_name='comment_on',on_delete=models.CASCADE)
    comment_at = models.DateTimeField(auto_now_add=True)

class MessageModel(models.Model):
    id = models.UUIDField(primary_key=True)
    message = models.CharField(max_length=250)
    sender = models.ForeignKey(UserModel,related_name='sender',on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserModel,related_name='receiver',on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    