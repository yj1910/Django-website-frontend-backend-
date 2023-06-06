from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class contacts(models.Model):
    name=  models.CharField(max_length=30)
    email= models.CharField(max_length=30)
    phone= models.CharField(max_length=30)
    desc= models.CharField(max_length=300)
    date= models.DateField()

    def __str__(self):
        return self.name
