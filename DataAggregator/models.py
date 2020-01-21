from django.db import models

# Create your models here.


class Coach(models.Model):
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    secondName = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    birthDate = models.DateField()
    sport = models.CharField(max_length=200)
    seniorityPeriod = models.IntegerField()
    citizenship = models.CharField(max_length=30)
    publicPhone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    attestation = models.CharField(max_length=200)
    jobInfo = models.CharField(max_length=200)
    coachCategory = models.CharField(max_length=200)
    sportSpecialization = models.CharField(max_length=100)
    sportActivityGender = models.CharField(max_length=20)
    sportActivityMinAge = models.IntegerField()
    globalId = models.CharField(max_length=100)
