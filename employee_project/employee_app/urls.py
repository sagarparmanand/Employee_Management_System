from django.urls import path
from employee_app import views
urlpatterns = [
    path('',views.home),
    path('emp',views.employee_management),
    path('emp_add',views.employee_management_add),
    path('emp_del/<did>',views.employee_management_del),
    path('emp_up/<uid>',views.employee_management_up),

    path('dep',views.department_management),
    path('dep_add',views.department_management_add),
    path('del/<did>',views.department_management_del),
    
    path('sal',views.salary_management),
    path('sal_add',views.salary_management_add),
    path('sal_up/<uid>',views.salary_management_up),
    path('sal_cal',views.salary_management_cal),
]
