from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Founder(models.Model):
    CHOICE_B2B = 'B2B'
    CHOICE_B2C = 'B2C'

    CHOICES = [
        (CHOICE_B2B, 'B2B'),
        (CHOICE_B2C, 'B2C'),
    ]

    user = models.OneToOneField(User, related_name='Founder', on_delete=models.CASCADE)
    startupName = models.CharField(max_length=255, null=True, blank=True)
    websiteUrl = models.URLField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255),
    business = models.CharField(max_length=3, choices=CHOICES, null=True, blank=True)
    annualRevenue = models.FloatField(null=True, blank=True)
    productType = models.CharField(max_length=255,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=255)


class Employee(models.Model):
    CHOICE_MENTOR = 'MENTOR'
    CHOICE_TALENT = 'TALENT'

    CHOICES = [
        (CHOICE_MENTOR, 'MENTOR'),
        (CHOICE_TALENT, 'TALENT')
    ]

    user = models.OneToOneField(User, related_name='Mentor', on_delete=models.CASCADE)
    speciality = models.CharField(max_length=255,null=True, blank=True)
    city = models.CharField(max_length=255)
    hourlyRate = models.FloatField(null=True, blank=True)
    role = models.CharField(max_length=7, choices=CHOICES)
    phone_number = models.CharField(max_length=255, label='Phone Number')



class Skill(models.Model):
    skillName = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, related_name='Skill', on_delete=models.CASCADE)


class Investor(models.Model):
    user = models.OneToOneField(User, related_name='Investor', on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, label='Phone Number')





