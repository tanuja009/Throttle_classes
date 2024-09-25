from django.contrib import admin
from django.urls import path
from app2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.studentlist.as_view(),name="student")
]
