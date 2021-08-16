from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import IntegrityError
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.db.models.deletion import CASCADE


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name =models.CharField(max_length=144,null=True,blank=True)
    last_name = models.CharField(max_length=144,null=True,blank=True)


    def delete_user(self):
        self.delete()

# Create your models here.
class Country(models.Model):
  iso_code = models.CharField(max_length=20)
  name = models.CharField(max_length=30)

  def save_country(self):
    self.save()

  def delete_country(self):
    self.delete()

  def __str__(self):
    return self.name

class Intervention(models.Model):
  office_id = models.ForeignKey(Country,on_delete=CASCADE)
  name = models.CharField(max_length=30)
  code_name = models.CharField(max_length=20)
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()

  def save_office(self):
    self.save()

  def delete_office(self):
    self.delete()

  def __str__(self):
    return self.name