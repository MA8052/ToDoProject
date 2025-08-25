from django.db import models

# Create your models here.
class ToDoTable(models.Model):
    Task_column=models.CharField(max_length=50)

    def __str__(self):
        return self.Task_column
    

