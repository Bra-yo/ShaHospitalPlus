from django.db import models

# Create your models here.
class Patient(models.Model):
    name =models.CharField(max_length=100)
    age =models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    message = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name



class Doctor(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    email = models.EmailField()
    department = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class Staff(models.Model):
   FirstName = models.CharField(max_length = 50)
   LastName = models.CharField(max_length = 50)
   Position = models.CharField(max_length = 50)
   PhoneNumber = models.CharField(max_length = 10)
   Email = models.EmailField()
   HireDate = models.DateField()

   def __str__(self):
        return self.FirstName+" "+self.LastName

class Ward(models.Model):
   Name = models.CharField(max_length = 50)
   TotalBeds = models.IntegerField()
   AvailableBeds = models.IntegerField()


   def __str__(self):
        return self.Name