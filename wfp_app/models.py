from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Country(models.Model):
  iso_code = models.CharField(max_length=20)
  name = models.CharField(max_length=30)

class Intervention(models.Model):
  office_id = models.ForeignKey(Country,on_delete=CASCADE)
  name = models.CharField(max_length=30)
  code_name = models.CharField(max_length=20)
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()
