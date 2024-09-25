from django.db import models

# Create your models here.
class student(models.Model):
  subjects = [
    ('maths', 'Maths'),
    ('english', 'English'),
    ('physics', 'Physics'),
    ('chemistry', 'Chemistry'),
    ('bio', 'Biology')
   ]
  gender=[
    ('boy','boy'),
    ('girl','girl'),
    ('other','other')
  ]
  name=models.CharField(max_length=50)
  age=models.IntegerField()
  subject=models.CharField(choices=subjects,max_length=40)
  gender=models.CharField(choices=gender,max_length=50)

  def __str__(self):
        return f"{self.name}"  # Customize this string as needed