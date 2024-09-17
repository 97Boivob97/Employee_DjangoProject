from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def homepage(request):
   employees = Employee.objects.all()
   context = {"employees":employees}
   return render(request,'homepage.html',context)

def employee_details(request, pk):
    try: 
        employee = Employee.objects.get(pk=pk)
        context = {
            "employee": employee,
        }
        return render(request, 'employee_details.html', context=context)
    except Employee.DoesNotExist:
        return HttpResponse("Employee does not exist")

def add(request):
   if request.method == "POST":
      form = EmployeeForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('homepage')
   else:
      form = EmployeeForm()
      context = {"form":form}
      return render(request,'add_employee.html',context)
   
def delete(request,pk):
   try:
      employee = Employee.objects.get(pk=pk)
      employee.delete()
      return redirect('homepage')
   except Employee.DoesNotExist:
      return HttpResponse("Employee Does Not Exists!")
   
def update(request,pk):
    try:
        employee = Employee.objects.get(pk=pk)
        if request.method == "POST":
            form = EmployeeForm(request.POST,instance=employee)
            if form.is_valid():
                form.save()
                return redirect('homepage')
            else:
                context = {
                    "form":form,
                }
                return render(request,'update.html',context)
        else:
            form = EmployeeForm(instance=employee)
            context = {
             "form":form
            }
            return render(request,'update.html',context)
    except Employee.DoesNotExist:
        return HttpResponse("Employee does not exists!")


   

