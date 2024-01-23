from django.contrib import admin
from employee_app.models import Employee,Salary
from dept_app.models import Department
# Register your models here.

admin.site.register(Employee)
admin.site.register(Salary)
admin.site.register(Department)