from django.urls import path
from .import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('add/',views.add,name="add"),
    path('delete/<int:pk>/',views.delete,name="delete"),
    path('update/<int:pk>/',views.update,name="update"),
    path('<int:pk>/',views.employee_details,name="employee_details"),
]