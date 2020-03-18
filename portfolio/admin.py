from django.contrib import admin
from .models import Project #from models folders import project class

admin.site.register(Project) #the model show up in the admin
