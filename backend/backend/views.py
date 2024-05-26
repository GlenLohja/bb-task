from rest_framework import generics
from .models import Customer, LoanOffer
from django.http import JsonResponse
from rest_framework.decorators import api_view
import math
from .serializers import CustomerSerializer, LoanOfferSerializer

class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class LoanOfferCreateView(generics.CreateAPIView):
    queryset = LoanOffer.objects.all()
    serializer_class = LoanOfferSerializer
    

@api_view(['POST'])
def loan_calculator(request):
    """
    Calculate monthly loan payments using the standard loan amortization formula.
    Expected JSON payload:
    {
        "loan_amount": 10000.00,
        "interest_rate": 5.5,
        "loan_term": 24
    }
    """
    try:
        loan_amount = float(request.data.get('loan_amount'))
        interest_rate = float(request.data.get('interest_rate'))
        loan_term = int(request.data.get('loan_term'))

        # Validate input values
        if loan_amount <= 0:
            return JsonResponse({'loan_amount': 'Loan amount must be a positive value.'}, status=400)
        if interest_rate < 0:
            return JsonResponse({'interest_rate': 'Interest rate must be a non-negative value.'}, status=400)
        if loan_term <= 0:
            return JsonResponse({'loan_term': 'Loan term must be a positive value.'}, status=400)

        # Convert annual interest rate to a monthly rate
        monthly_rate = interest_rate / 100 / 12
        # Calculate monthly payment using the loan amortization formula
        if monthly_rate == 0:  # handle the case of zero interest rate
            monthly_payment = loan_amount / loan_term
        else:
            monthly_payment = loan_amount * (monthly_rate * math.pow(1 + monthly_rate, loan_term)) / (math.pow(1 + monthly_rate, loan_term) - 1)

        monthly_payment = round(monthly_payment, 2)
        return JsonResponse({'monthly_payment': monthly_payment}, status=200)

    except (ValueError, TypeError):
        return JsonResponse({'error': 'Invalid input values'}, status=400)