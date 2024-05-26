from django.urls import path
from .views import CustomerCreateView, CustomerDetailView, LoanOfferCreateView, loan_calculator

urlpatterns = [
    path('customers', CustomerCreateView.as_view(), name='customer-create'),
    path('customers/<int:pk>', CustomerDetailView.as_view(), name='customer-detail'),
    path('loanoffers', LoanOfferCreateView.as_view(), name='loanoffer-create'),
    path('loan-calculator', loan_calculator, name='loan-calculator'),
]