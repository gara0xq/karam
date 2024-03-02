from django.db import models
from datetime import date

# Create your models here.
class Employee(models.Model):
    #postion choices
    position_choiced = (
        ('employee', 'employee'),
        ('semi_manager', 'semi_manager'),
        ('leader', 'leader'),
    )

    #model
    code = models.IntegerField()
    name = models.CharField(max_length = 225)
    password = models.CharField(max_length = 225)
    position = models.CharField(max_length=50, choices=position_choiced)
    salary = models.IntegerField()
    profile_image = models.ImageField(upload_to='images/')
    browing_lim = models.IntegerField()
    normal_vecation = models.IntegerField()
    casual_vecation = models.IntegerField()
    manager_code = models.IntegerField()

class Manager(models.Model):
    #model
    code = models.IntegerField()
    name = models.CharField(max_length = 225)
    password = models.CharField(max_length = 225)
    salary = models.IntegerField()
    profile_image = models.ImageField(upload_to='images/')
    browing_lim = models.IntegerField()
    normal_vecation = models.IntegerField()
    casual_vecation = models.IntegerField()


class Brawing(models.Model):
    #approved choices
    approved_choiced = (
        ('yes', 'yes'),
        ('no', 'no'),
        ('in_wait', 'in_wait'),
    )
    approved_defualt = 'in_wait' #defualt choice

    date = models.DateField(auto_now_add=True)
    emp_code = models.IntegerField()
    manager_code = models.IntegerField()
    amount = models.IntegerField()
    approved = models.CharField(max_length=50, choices=approved_choiced, default=approved_defualt)



class Vecation(models.Model):
    #approved choices
    approved_choiced = (
        ('yes', 'yes'),
        ('no', 'no'),
        ('in_wait', 'in_wait'),
    )
    approved_defualt = 'in_wait' #defualt choice

    #vec type choices
    vecation_type_choiced = (
        ('normal', 'normal'),
        ('casual', 'casual'),
    )

    #model
    vecation_type = models.CharField(max_length = 50, choices=vecation_type_choiced)
    from_date = models.DateField(default=date.today)
    to_date = models.DateField()
    emp_code = models.IntegerField()
    manager_code = models.IntegerField()
    approved = models.CharField(max_length=50, choices=approved_choiced, default=approved_defualt)

    