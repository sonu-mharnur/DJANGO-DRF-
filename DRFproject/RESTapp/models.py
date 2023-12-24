from django.db import models

# Create your models here.

class Student(models.Model):
    Name= models.CharField(max_length=100)
    Age = models.IntegerField(default=18)
    Father_name = models.CharField(max_length=100)

class Categoty(models.Model):
    Categoty_name = models.CharField(max_length=100)

class Book(models.Model):
    
    category = models.ForeignKey(Categoty, on_delete=models.CASCADE)

    book_title = models.CharField(max_length=100)