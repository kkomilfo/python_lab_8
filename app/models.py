from django.db import models

# Create your models here.
class Patient(models.Model):
    card_number = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    birth_year = models.IntegerField()

    # Category choices: child or adult
    CATEGORY_CHOICES = [
        ('child', 'Child'),
        ('adult', 'Adult'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Doctor(models.Model):
    doctor_code = models.AutoField(primary_key=True)  # AutoField automatically increments
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    experience_years = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class HospitalStay(models.Model):
    stay_code = models.AutoField(primary_key=True)
    patient_card_number = models.ForeignKey('Patient', on_delete=models.CASCADE)  # Foreign key to Patient model
    admission_date = models.DateField()
    days_in_hospital = models.IntegerField()
    daily_cost = models.FloatField()
    discount_percent = models.FloatField()
    doctor_code = models.ForeignKey('Doctor', on_delete=models.CASCADE)  # Foreign key to Doctor model

    def __str__(self):
        return f"Stay Code: {self.stay_code} - Patient: {self.patient_card_number} - Doctor: {self.doctor_code}"