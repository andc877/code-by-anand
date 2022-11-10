from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    GENDER_CHOICES =(('M',"MALE"),('F',"FEMALE"))

    user =models.ForeignKey(User,on_delete=models.CASCADE)
    # DOB =
    # Phone =
    # Address =
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    city= models.TextField(max_length=30,default="not available")
    created_on =models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['-created_on']
        verbose_name ='UserProfile'
        verbose_name_plural ='UserProfiles'


    def _str_(self):
        return self.user.username
    
    
    
    
    
    
  

    
    # class Category(models.Model):                                                    2

    # Title =models.CharField(max_length=100,default='')    
    # Detail = models.CharField(max_length=1,)
    # Image=models.FilePathField(path='/img',default='/img/noimage.png')     
    # Added_on =models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering =['-Added_on']
    #     verbose_name ='Category'
    #     verbose_name_plural ='Categories'


    # def _str_(self):
    #     return self.user.category



    # class AIModel(models.Model):                                                          3
   
    # File = models.CharField(max_length=1,choices=GENDER_CHOICES)
    # Description = models.CharField(max_length=1,choices=GENDER_CHOICES)
    # Uploaded_by =models.ForeignKey(User,on_delete=models.CASCADE)
    # Uploaded_on = models.CharField(max_length=1,choices=GENDER_CHOICES)
    # Category  =models.ForeignKey(User,on_delete=models.CASCADE)
    # Size= models.TextField(max_length=30,default="not available")
    # install= models.TextField(max_length=30,default="not available")
    # Size= models.TextField(max_length=30,default="not available")
    # created_on =models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering =['-created_on']
    #     verbose_name ='AIModel'
    #     verbose_name_plural ='AIModels'


    # def _str_(self):
    #     return self.user.AIModel



    # class Download(models.Model):                                                        4
   

    # Model =models.ForeignKey(User,on_delete=models.CASCADE)
    # User =models.ForeignKey(User,on_delete=models.CASCADE)
    # Downloaded_on =models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering =['-Downloaded_on']
    #     verbose_name ='Download'
    #     verbose_name_plural ='Downloads'


    # def _str_(self):
    #     return self.user.download



    # class Rating(models.Model):                                                        5
   
    # Model =models.ForeignKey(User,on_delete=models.CASCADE)
    # User =models.ForeignKey(User,on_delete=models.CASCADE)
    # Rating = models.CharField(max_length=1,choices=GENDER_CHOICES)
    # Review= models.TextField(max_length=30,default="not available")
    # Review_on =models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering =['-created_on']
    #     verbose_name ='Rating'
    #     verbose_name_plural ='Ratings'


    # def _str_(self):
    #     return self.user.rating