from django.contrib import admin
from .models import Customer, LoanOffer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

@admin.register(LoanOffer)
class LoanOfferAdmin(admin.ModelAdmin):
    list_display = ('customer', 'loan_amount', 'interest_rate', 'loan_term')