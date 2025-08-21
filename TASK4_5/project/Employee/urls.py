from django.urls import path
from .views import EmployeeView,Dep_view

urlpatterns = [
    path("employees/", EmployeeView.as_view(), name="employee-list"),
    path("Department", Dep_view.as_view(), name="employee-list"),
]
