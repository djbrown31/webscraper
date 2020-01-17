from django.conf import settings
from django.db import models
from faker import Faker

class Cohort(models.Model):
    cohort_name = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)

    def __str__(self):
        return f"id={self.id}, cohort_name={self.cohort_name}, start_date={self.start_date}, end_date={self.end_date}"

class Student(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='students')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"id={self.id}, first_name={self.first_name}, last_name={self.last_name}"



# Create your models here.
fake = Faker()
for _ in range(10):
    cohort = Cohort(cohort_name=fake.word(), start_date=fake.date(), end_date=fake.date())
    cohort.save()
    for _ in range(10):
        student = Student(first_name=fake.first_name(), last_name=fake.last_name(), cohort=cohort)
        student.save()
