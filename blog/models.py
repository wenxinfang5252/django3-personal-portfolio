from django.db import models

class Blog(models.Model): #set databse attributs
    title = models.CharField(max_length = 200)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title #show its project name in admin page; no need to make migrations 
