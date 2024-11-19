# Ex02 Django ORM Web Application
## Date: 19.11.2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![Screenshot 2024-11-15 205242](https://github.com/user-attachments/assets/8e05492c-c79f-4583-9fdb-50a3036d28d5)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
'''
admin.py

from django.contrib import admin
from .models import bankloan,bankloanAdmin
admin.site.register(bankloan,bankloanAdmin)

models.py

from django.db import models
from django.contrib import admin
class bankloan (models.Model):
    Bank_ID=models.IntegerField(primary_key=True)
    Bank_name=models.CharField(max_length=100)
    Customer_name=models.CharField(max_length=100)
    Loan_amount=models.IntegerField()
    Customer_mobile_number=models.IntegerField()
    Loan_Date=models.DateField()
 
class bankloanAdmin(admin.ModelAdmin):
    list_display=('Bank_ID','Bank_name','Customer_name','Loan_amount','Customer_mobile_number','Loan_Date')
'''


## OUTPUT
![alt text](<Screenshot 2024-11-19 212017.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
