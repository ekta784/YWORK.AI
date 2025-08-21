from django.urls import path
urlpatterns = [
    path('employee' , Employeeview.as_view())
]