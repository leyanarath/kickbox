from django.db import models

# Create your models here.
class banner(models.Model):
    name=models.CharField(max_length=150)
    img=models.ImageField(upload_to='pics')
    details=models.TextField()
    def __str__(self):
        return self.name
class review(models.Model):
    name=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='pics')
    feedback=models.TextField()
    def __str__(self):
        return self.name
