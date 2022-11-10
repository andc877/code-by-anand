from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MinValueValidator,MaxValueValidator


# Create your models here.

class AiModel(models.Model):
    
    """Model definition for AIModel."""

    model_category =(
        (1,"image"),
        (2,"text"),
        (3,"nlp"),
        (4,"video"),
        (5,"others"),

    )

    name = models.CharField(max_length=225,default='model')
    summary = models.TextField()
    model_file =models.FileField(upload_to='ai_models',null=True)
    category= models.IntegerField(choices=model_category,default=model_category[0][1])
    model_image = models.ImageField(upload_to='ai_models/images',null=True)
    uploader =models.ForeignKey(User,on_delete=models.DO_NOTHING,default=2)
    uploaded_on =models.DateTimeField(auto_now=True) 
       
  

    def __str__(self):
        return self.name



class ModelEditForm(models.Model):
    """Model definition for AIModel."""

    model_category =(
        (1,"image"),
        (2,"text"),
        (3,"nlp"),
        (4,"video"),
        (5,"others"),

    )

    name = models.CharField(max_length=225,default='model')
    summary = models.TextField()
    model_file =models.FileField(upload_to='ai_models',null=True)
    category= models.IntegerField(choices=model_category,default=model_category[0][1])
    model_image = models.ImageField(upload_to='ai_models/images',null=True)
    uploader =models.ForeignKey(User,on_delete=models.DO_NOTHING,default=2)
    uploaded_on =models.DateTimeField(auto_now=True) 
       
  

    def __str__(self):
        return self.name




class ReviewAiModel(models.Model):
    title = models.CharField(max_length=225,default="review title")
    detail = models.TextField()
    reviewer = models.ForeignKey(User,on_delete=models.DO_NOTHING,)
    aimodel = models.ForeignKey(AiModel,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=3,validators=[MinValueValidator(1),MaxValueValidator(5)])
    uploaded_on =models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f'{self.title} for {self.aimodel}'
    
    
    
    
  
class ContactModel(models.Model):
    Name = models.CharField(max_length=225,)
    Email = models.EmailField(max_length=225,)
    Subject = models.CharField(max_length=225,)
    Message = models.TextField()
    
    def __str__(self):
        return self.name

    
    
    
    
    