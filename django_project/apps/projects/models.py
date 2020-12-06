from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    body = models.TextField()
    technology = models.ManyToManyField('Technology', related_name='projects')
    image = models.CharField(max_length=100)
    
    # returns name/title of object instead of 'object (#)'
    def __str__(self):
        return self.title #or self.title for blog posts

class Technology(models.Model):
    name = models.CharField(max_length=20)
    
    # returns name/title of object instead of 'object (#)'
    def __str__(self):
        return self.name