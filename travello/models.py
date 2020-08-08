from django.db import models

# Create your models here.
class app(models.Model):

    name = models.CharField(max_length=50)
    desc =  models.TextField()
    img =  models.ImageField(upload_to='pics') 
    offer = models.BooleanField(default=False)
