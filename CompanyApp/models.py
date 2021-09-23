from django.db import models

# Create your models here.

class Products (models.Model):
    ProductId = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=100)
    ProductDescription = models.CharField(max_length=100)
    ProductPrice = models.CharField(max_length=50)
    PhotoFileName = models.CharField(max_length=100)

class Companies (models.Model):
    CompanyID = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=100)
    CompanyCNPJ = models.CharField(max_length=20)
    CompanyDepartment = models.CharField(max_length=50)
    CompanyAdress = models.CharField(max_length=100)
    PhotoFileName = models.CharField(max_length=100)
