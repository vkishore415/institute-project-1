from django.db import models
import datetime
from multiselectfield import MultiSelectField

# Create your models here.
class FeedBackData(models.Model):
    name=models.CharField(max_length=50)
    rating=models.IntegerField()
    date=models.DateTimeField()
    feedback=models.TextField(max_length=500)




class ContactFormData(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    LOCATION_CHOICES=(
        ('HYD','HYDERABAD'),
        ('PUNE','PUNE')
    )
    location=MultiSelectField(max_length=50,choices=LOCATION_CHOICES)
    COURSES_CHOICES=(
        ('PYTHON','PYTHON'),
        ('DJANGO','DJANGO')
    )
    courses=MultiSelectField(max_length=200,choices=COURSES_CHOICES)
    SHIFT_CHOICES=(
        ('MRNG','MORNING'),
        ('EVE','EVENINNG')
    )
    shifts=MultiSelectField(max_length=100,choices=SHIFT_CHOICES)
    gender=models.CharField(max_length=20)
    start_date=models.DateField(max_length=100)


class CoursesData(models.Model):
    courses_id=models.IntegerField()
    courses_name=models.CharField(max_length=100)
    courses_dur=models.IntegerField()
    courses_fee=models.IntegerField()
    start_date=models.DateField(max_length=100)
    start_time=models.TimeField(max_length=100)
    trainer_name=models.CharField(max_length=100)
    trainer_exp=models.IntegerField()
