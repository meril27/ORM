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
