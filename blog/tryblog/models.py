from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # this is to send redirect to article page
        # return reverse('article-detail',args=(str(self.id)) ) 
        return reverse('home')



class Post(models.Model):
    title=models.CharField(max_length=255)
    title_tag=models.CharField(max_length=255) #, default="GOOD BLOG" also can be used
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True,null=True)
    publication_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    likes = models.ManyToManyField(User,related_name='blog_post')

    snippet = models.CharField(max_length=255)

    header_image = models.ImageField(null=True, blank=True, upload_to = "images/")



    def total_likes(self):
        return self.likes.count()

    
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # this is to send redirect to article page
        # return reverse('article-detail',args=(str(self.id)) ) 
        return reverse('home')


# TO edit user profile
class Profile(models.Model):
    user = models.OneToOneField(User, null=True ,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True,blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255,null=True,blank=True)
    facebook_url = models.CharField(max_length=255,null=True,blank=True)    
    instagram_url = models.CharField(max_length=255,null=True,blank=True)    
    twitter_url = models.CharField(max_length=255,null=True,blank=True)    


    def __str__(self):
        return str(self.user) 

    def get_absolute_url(self):
        # this is to send redirect to article page
        # return reverse('article-detail',args=(str(self.id)) ) 
        return reverse('home')