from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    
    # returns name/title of object instead of 'object (#)'
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    # returns name/title of object instead of 'object (#)'
    def __str__(self):
        return self.title #or self.name