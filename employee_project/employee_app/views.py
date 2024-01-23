from django.shortcuts import render,HttpResponse,redirect
from employee_app.models import Employee, Department, Salary
from django.db.models import Sum, Case, When, Value, IntegerField
# Create your views here.

def home(request):
    context={}
    d=Employee.objects.all()
    context['data']=d
    result = Department.objects.values('name').annotate(
    TotalSalary=Sum(
        Case(
            When(employee__salary__amount__isnull=True, then=Value(0)),
            default='employee__salary__amount',
            output_field=IntegerField()
        )
    )
)   
    context['tot']=result
    return render(request,'home.html',context)

def employee_management(request):
    context={}
    if request.method=='GET':
        d=Employee.objects.all()
        context['data']=d
        return render(request,'emp/emp_list.html',context)
    
def employee_management_add(request):
    context={}
    dp=Department.objects.all()
    emp=Employee.objects.all()
    if request.method=='GET':
        context['data']=dp
        context['edata']=emp
        return render(request,'emp/emp_add.html',context)
    else:
        uname=request.POST['uname']
        email=request.POST['email']
        uadd=request.POST['uadd']
        des=request.POST['des']
        rep_man=request.POST['rep_man']
        dep=request.POST['dep']
        obj_m=Employee.objects.get(id=rep_man)
        o_name=obj_m.name
        print(o_name)
        obj_d=Department.objects.get(id=dep)
        em=Employee.objects.create(name=uname,email=email,address=uadd,designation=des,reporting_manager=o_name,department=obj_d)
        em.save()
        return redirect('/emp')
    
def employee_management_up(request,uid):
    context={}
    if request.method=='GET':
        d=Employee.objects.get(id=uid)
        dp=Employee.objects.all()
        dpp=Department.objects.all()
        context['data']=d
        context['ddata']=dp
        context['idata']=dpp
        return render(request,'emp/emp_up.html',context)
    else:
        d=Employee.objects.filter(id=uid)
        uname=request.POST['uname']
        email=request.POST['email']
        uadd=request.POST['uadd']
        des=request.POST['des']
        rep_man=request.POST['rep_man']
        dep=request.POST['dep']
        obj_m=Employee.objects.get(id=rep_man)
        o_name=obj_m.name
        print(o_name)
        obj_d=Department.objects.get(id=dep)
        d.update(name=uname,email=email,address=uadd,designation=des,reporting_manager=o_name,department=obj_d)
        return redirect('/emp')

def employee_management_del(request,did):
    d=Employee.objects.get(id=did)
    d.delete()
    return redirect('/emp')

def department_management(request):
    context={}
    if request.method=='GET':
        d=Department.objects.all()
        context['data']=d
        return render(request,'dep/dep_list.html',context)
    
def department_management_del(request,did):
    d=Department.objects.get(id=did)
    d.delete()
    return redirect('/dep')

def department_management_add(request):
    if request.method=='GET':
        return render(request,'dep/dep_add.html')
    else:
        dname=request.POST['dname']
        floor=request.POST['floor']

        s=Department.objects.create(name=dname,floor=floor)
        s.save()
        return redirect('/dep')

def salary_management(request):
    context={}
    if request.method=='GET':
        d=Salary.objects.all()
        context['data']=d
        return render(request,'sal/sal_list.html',context)
    
def salary_management_add(request):
    context={}
    if request.method=='GET':
        em=Employee.objects.all().order_by('-name')
        context['edata']=em
        return render(request,'sal/sal_add.html',context)
    else:
        uname=request.POST['uname']
        obj=Employee.objects.get(id=uname)
        sdate=request.POST['sdate']
        edate=request.POST['edate']
        sal=request.POST['sal']

        s=Salary.objects.create(employee=obj,start_date=sdate,end_date=edate,amount=sal)
        s.save()
        return redirect('/sal')

def salary_management_up(request,uid):
    if request.method=='GET':
        context={}
        s=Salary.objects.get(id=uid)
        e=Employee.objects.all()
        context['data']=s
        context['edata']=e
        return render(request,'sal/sal_up.html',context)
    else:
        uname=request.POST['uname']
        obj=Employee.objects.get(id=uname)
        sdate=request.POST['sdate']
        edate=request.POST['edate']
        sal=request.POST['sal']

        s=Salary.objects.filter(id=uid)
        s.update(employee=obj,start_date=sdate,end_date=edate,amount=sal)
        return redirect('/sal')
    
def salary_management_del(request,did):
    s=Salary.objects.get(id=did)
    s.delete()
    return redirect('/sal')

def salary_management_cal(request):
    if request.method == 'POST':
        context={}
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        department_costs = Salary.objects.filter(end_date__range=[start_date, end_date]) \
            .values('employee__department__name') \
            .annotate(total_cost=Sum('amount'))
        d=Salary.objects.all()
        context['data']=d
        context['department_costs']=department_costs

        return render(request, 'sal/sal_list.html', context)

    return render(request, 'sal/sal_list.html')