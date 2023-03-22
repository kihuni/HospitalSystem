from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    gender = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    birthdate = models.DateField()
    bloodgroup = models.CharField(max_length=5)
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Receptionist(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    gender = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    birthdate = models.DateField()
    bloodgroup = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    gender = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self):
        return self.name

class Appoitment(models.Model):
    doctorname = models.CharField(max_length=50)
    doctoremail = models.EmailField(max_length=50)
    patientname = models.CharField(max_length=50)
    patientemail = models.EmailField(max_length=50)
    Appoitmentdate = models.DateField(max_length=10)
    Appoitmenttime = models.TimeField(max_length=100)
    symptoms = models.BooleanField()
    prescription = models.CharField(max_length=200)

    def __str__(self):
        return self.patientname+ "you have appoitment with "+self.doctorname
