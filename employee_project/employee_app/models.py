from django.db import models
from dept_app.models import Department

# Create your models here.

class Employee(models.Model):
    DESIGNATION_CHOICES = (
        ('Associate', 'Associate'),
        ('TL', 'Team Lead'),
        ('Manager', 'Manager'),
        ('Admin', 'Admin'),
    )

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    designation = models.CharField(max_length=20, choices=DESIGNATION_CHOICES)
    # reporting_manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    reporting_manager = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE ,null=True ,blank=True)

    def __str__(self):
        return str(self.reporting_manager)

class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True ,blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    amount = models.FloatField()

    def __str__(self):
        return f"{self.employee} - {self.amount}"