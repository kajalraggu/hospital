from django.db import models

# Create your models here.

class Patients(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=300)
    patient_age = models.SmallIntegerField()
    patient_gender = models.CharField(max_length=30)
    patient_city = models.CharField(max_length=300)
    patient_email = models.EmailField(max_length=300)
    patient_phone = models.CharField(max_length=10)
    patient_image = models.ImageField(null=True, upload_to='patients/')
    patient_symptoms = models.CharField(max_length=3000)
    
    
