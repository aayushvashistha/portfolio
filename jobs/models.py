from django.db import models

# Create your models here.

class job(models.Model):
    image = models.ImageField(upload_to='images')
    summary = models.CharField(max_length=200)
    # slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.summary
    
class resume(models.Model):
    year = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)

    # def __str__(self):
    #     return self.year