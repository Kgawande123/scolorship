from django.db import models

# Create your models here.
class Scolorship(models.Model):
    Id = models.IntegerField(primary_key=True)
    First_Name = models.CharField(max_length=23)
    Middle_Name = models.CharField(max_length=23)
    Last_Name = models.CharField(max_length=23)
    Address = models.CharField(max_length=34)
    Mobile_NO=models.BigIntegerField()
    Date_Of_Birth = models.DateField()
    Age = models.IntegerField()
    Profile_Picture = models.ImageField(upload_to="profiles/",)



