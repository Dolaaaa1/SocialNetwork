from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.


class User(AbstractUser):
    profile_pic =models.ImageField(default='profile_pics/default.jpg',upload_to='profile_pics')
    bio = models.TextField(blank=True,null=True ,max_length=500 , default="")
    
    def get_num_posts(self):
        return Post.objects.filter(user=self).count()
    
    def is_following(self , user_B):
        count = Friends.objects.filter(user_a=self ,user_b=user_B).count()
        if count > 0 :
            return True
        else:
            return False
        
        
    def get_followings(self):
        followings = Friends.objects.filter(user_a =self)
        temp =[]
        for item in followings:
            temp.append(item.user_b.id)
        return temp        
         
    
    
    
    
    
class Post(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    caption = models.TextField(max_length=600 , null=False)
    date_created = models.DateTimeField(auto_now_add=True , null=False)
    
    
    def __str__(self):
        return self.caption    
    
    
    
class Friends(models.Model):
    user_a = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_a') 
    user_b = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_b')  
    
    
    def __str__(self):
        return self.user_a.username + " --- "+ self.user_b.username
    
