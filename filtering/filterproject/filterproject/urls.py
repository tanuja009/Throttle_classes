from django.contrib import admin
from django.urls import path
from filterapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employeeapi/',views.employeelist.as_view()),
]
