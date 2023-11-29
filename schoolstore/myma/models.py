from django.db import models

# Create your models here.


class Department(models.Model):
    department=models.CharField(max_length=20)
    def __str__(self):
        return '{}'.format(self.department)
class Courses(models.Model):
    courses=models.CharField(max_length=20)
    def __str__(self):
        return '{}'.format(self.courses)
class Enquiry(models.Model):
    enquiry=models.CharField(max_length=20)
    def __str__(self):
        return '{}'.format(self.enquiry)

class Student(models.Model):
    name = models.CharField(max_length=250)
    Dob = models.DateField()
    TYPE_SELECT = (('0', 'Female'), ('1', 'male'),)
    gender = models.CharField(max_length=11, choices=TYPE_SELECT)
    phonenumber=models.CharField(max_length=10)
    email=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    courses=models.ForeignKey(Courses,on_delete=models.CASCADE)
    enquiry=models.ForeignKey(Enquiry,on_delete=models.CASCADE)


    def __str__(self):
        return '{}'.format(self.name)