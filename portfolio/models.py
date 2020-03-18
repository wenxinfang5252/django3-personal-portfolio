from django.db import models

class Project(models.Model): #set databse attributs
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    image = models.ImageField(upload_to = 'portfolio/images/')
    url = models.URLField(blank = True) #url is optional

    def __str__(self):
        return self.title #show its project name in admin page 
