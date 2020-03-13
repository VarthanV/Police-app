from django.db import models

class Police(models.Model):
    unique_id = models.CharField(max_length=100)
    name =models.CharField(max_length=50)
    station =models.CharField(max_length=100)
    age = models.IntegerField()
    department =models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.name
