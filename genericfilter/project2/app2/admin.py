from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(student)
class studentlistapi(admin.ModelAdmin):
  list_display=['id','name','age','city','passby']