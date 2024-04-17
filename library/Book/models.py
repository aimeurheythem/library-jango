from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.TextChoices):
    MATH = 'math'
    SCIENCE = 'science'
    PHYSICS = 'physics'
    ARABIC = 'arab'
    ISLAMIC = 'islamic'
    FRENSH = 'frensh'
    GEOGRAPHY = 'geography'
    HESTORY = 'hestory'


class Choices(models.TextChoices):
    RENTED = 'rented' 
    AVAILABLE = 'available'
    LOST = 'lost'

class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    author = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, default=0)
    category = models.CharField(max_length=100,choices=Category.choices)
    class_number = models.CharField(max_length=100, blank=True, null=True)
    entry_date = models.DateField(auto_now=False, blank=True, null=True)
    published_date = models.DateField(auto_now=False, blank=True, null=True)
    status = models.CharField(max_length=200, choices=Choices.choices, default='')
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.title
    

class Student(models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    adress = models.CharField(max_length=200, default='', blank=False)
    class_name = models.CharField(max_length=10, default='', blank=False)
    
    def __str__(self):
        return self.first_name

class Prof(models.Model):
    first_name = models.CharField(max_length=200, default='', blank=False)
    last_name = models.CharField(max_length=200, default='', blank=False)
    adress = models.CharField(max_length=200, default='', blank=True, null=True)
    phone_number = models.CharField(max_length=20, default=0, blank=True, null=True)

    def __str__(self):
        return self.first_name


class RentBook(models.Model):
    type = models.CharField(max_length=200, default='', blank=False)
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    prof_name = models.ForeignKey(Prof, on_delete=models.CASCADE, blank=True, null=True)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE, blank=False, default='')
    rent_date = models.DateField(auto_now_add=False)
    return_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.type
    

class Archive(models.Model):
    first_name = models.CharField(max_length=200, blank=False, default='')
    last_name = models.CharField(max_length=200, blank=False, default='')
    birth_date = models.DateField(default='')
    birth_place = models.CharField(max_length=50, default='')
    class_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.first_name