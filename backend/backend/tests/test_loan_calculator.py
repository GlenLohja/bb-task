from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# This class contains tests for the Loan Calculator API endpoint.
class LoanCalculatorTests(APITestCase):

    # The setUp method is called before each test. It sets up common test data and URLs.
    def setUp(self):
        # URL for the loan calculator endpoint
        self.url = reverse('loan-calculator')
        
        # Payload with valid loan data for testing the loan calculator endpoint
        self.valid_payload = {
            'loan_amount': 10000.00,
            'interest_rate': 5.5,
            'loan_term': 24
        }
        
        # Payload with an invalid loan amount (negative value)
        self.invalid_loan_amount_payload = {
            'loan_amount': -10000.00,
            'interest_rate': 5.5,
            'loan_term': 24
        }
        
        # Payload with an invalid interest rate (negative value)
        self.invalid_interest_rate_payload = {
            'loan_amount': 10000.00,
            'interest_rate': -5.5,
            'loan_term': 24
        }
        
        # Payload with an invalid loan term (negative value)
        self.invalid_loan_term_payload = {
            'loan_amount': 10000.00,
            'interest_rate': 5.5,
            'loan_term': -24
        }

    # Test calculating the monthly payment with valid data
    def test_calculate_monthly_payment_valid(self):
        # Send a POST request to calculate the monthly payment with valid data
        response = self.client.post(self.url, self.valid_payload, format='json')
        
        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Parse the response data
        response_data = response.json()
        
        # Assert that the response contains a 'monthly_payment' field
        self.assertIn('monthly_payment', response_data)
        
        # Assert that the calculated monthly payment is approximately the expected value
        self.assertAlmostEqual(response_data['monthly_payment'], 440.96, places=2)

    # Test calculating the monthly payment with an invalid loan amount (negative value)
    def test_calculate_monthly_payment_invalid_loan_amount(self):
        # Send a POST request to calculate the monthly payment with an invalid loan amount
        response = self.client.post(self.url, self.invalid_loan_amount_payload, format='json')
        
        # Assert that the response status code is 400 BAD REQUEST
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Parse the response data
        response_data = response.json()
        
        # Assert that the response contains the correct error message for 'loan_amount'
        self.assertIn('loan_amount', response_data)
        self.assertEqual(response_data['loan_amount'], 'Loan amount must be a positive value.')

    # Test calculating the monthly payment with an invalid interest rate (negative value)
    def test_calculate_monthly_payment_invalid_interest_rate(self):
        # Send a POST request to calculate the monthly payment with an invalid interest rate
        response = self.client.post(self.url, self.invalid_interest_rate_payload, format='json')
        
        # Assert that the response status code is 400 BAD REQUEST
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Parse the response data
        response_data = response.json()
        
        # Assert that the response contains the correct error message for 'interest_rate'
        self.assertIn('interest_rate', response_data)
        self.assertEqual(response_data['interest_rate'], 'Interest rate must be a non-negative value.')

    # Test calculating the monthly payment with an invalid loan term (negative value)
    def test_calculate_monthly_payment_invalid_loan_term(self):
        # Send a POST request to calculate the monthly payment with an invalid loan term
        response = self.client.post(self.url, self.invalid_loan_term_payload, format='json')
        
        # Assert that the response status code is 400 BAD REQUEST
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Parse the response data
        response_data = response.json()
        
        # Assert that the response contains the correct error message for 'loan_term'
        self.assertIn('loan_term', response_data)
        self.assertEqual(response_data['loan_term'], 'Loan term must be a positive value.')
