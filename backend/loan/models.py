from django.db import models
import math 

# Customer model
class Customer(models.Model):
    first_name = models.CharField(max_length=100) # required
    last_name = models.CharField(max_length=100) # required
    email = models.EmailField(unique=True) # required & unique

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Loan offers model
class LoanOffer(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) # required
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2) # required
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2) # required
    loan_term = models.IntegerField()  # in months # required

    def __str__(self):
        return f"Loan for {self.customer} - Amount: {self.loan_amount}"