from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    floor = models.IntegerField()
    # manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name