from django.db import models

# Create your models here.


class Employee(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    TITLE = (
        ('Owner', 'Owner'),
        ('CEO', 'CEO'),
        ('Manager', 'Manager'),
        ('Ass-Manager', 'Ass-Manager'),
        ('Clerk', 'Clerk'),
    )
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, null=True, choices=GENDER)
    title = models.CharField(max_length=50, null=True, choices=TITLE)
    occupation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    status = models.CharField(max_length=50, null=True, choices=STATUS)

    def __str__(self):
        return self.name
