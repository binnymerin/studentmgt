from django.db import models
#

class Registrations(models.Model):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    birth_date = models.CharField(max_length=50)
    pincode = models.IntegerField()
    Class = models.CharField(max_length=50)
    email = models.EmailField()
    password=models.CharField(max_length=50)

    rights = models.CharField(max_length=35, default='user')

    def __str__(self):
        return self.name

class teacherreg(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    birth_date = models.CharField(max_length=50)
    pincode = models.IntegerField()
    Class = models.CharField(max_length=50)
    subject =models.CharField(max_length=50,null=True)
    phoneno=models.IntegerField(null=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    rights = models.CharField(max_length=35, default='teacher')

    def __str__(self):
        return self.name
class Attendence(models.Model):
    date=models.DateField(auto_now_add=True)
    student=models.CharField(max_length=50)
    status=models.CharField(max_length=50,default="pending")
    def __str__(self):
        return self.student

class mark(models.Model):
    teacher=models.CharField(max_length=50)
    student=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    mark=models.CharField(max_length=50)
    grade=models.CharField(max_length=50)
    def __str__(self):
        return self.teacher

class leave(models.Model):
    teacher=models.CharField(max_length=50,null=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=50)
    date=models.DateField(max_length=50)
    reason=models.CharField(max_length=50)
    status=models.CharField(max_length=50,default='pending')
    def __str__(self):
        return self.name


class stdleave(models.Model):
    user=models.CharField(max_length=50,null=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=50)
    date=models.DateField(max_length=50)
    reason=models.CharField(max_length=50)
    status=models.CharField(max_length=50,default='pending')
    def __str__(self):
        return self.name

class timetable(models.Model):
    date=models.DateField(max_length=50)
    teachername=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    time=models.TimeField()
    def __str__(self):
        return f'{self.date}'