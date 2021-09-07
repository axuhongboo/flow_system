from django.db import models

# Create your models here.

class Pcaps_cut(models.Model):
    name = models.CharField(max_length=50, unique=True, primary_key=True)
    pub_date = models.DateField('date published')
    origin = models.CharField(max_length=100, default="wrong")
    label = models.CharField(max_length=100, default="test")
    type = models.CharField(max_length=20, default="flow")
    def __str__(self):
        return self.name