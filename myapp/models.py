from django.db import models 

# Create your models here.
class ToDoList( models.Model ):
    taskname=models.CharField(max_length=200)
    enddate=models.CharField(max_length=200)
    iscomplete=models.BooleanField(default=False)

  

