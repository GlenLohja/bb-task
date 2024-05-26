from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from loan.models import Customer

# This class contains tests for the Loan Offer creation API endpoint.
class LoanOfferTests(APITestCase):

    # The setUp method is called before each test. It sets up common test data and URLs.
    def setUp(self):
        # URL for creating a new loan offer
        self.loan_offer_url = reverse('loanoffer-create')
        
        # Payload with valid customer data for creating a test customer
        self.valid_customer_payload = {
            'first_name': 'Glen',
            'last_name': 'Lohja',
            'email': 'glenlohja@example.com'
        }
        
        # Create a test customer in the database
        self.customer = Customer.objects.create(**self.valid_customer_payload)
        
        # Payload with valid loan offer data, using the test customer's ID
        self.valid_loan_offer_payload = {
            'customer': self.customer.id,
            'loan_amount': 10000.00,
            'interest_rate': 5.5,
            'loan_term': 24
        }
        
        # Payload with invalid loan offer data (non-existent customer ID)
        self.invalid_loan_offer_payload = {
            'customer': 999,  # Non-existent customer ID
            'loan_amount': 10000.00,
            'interest_rate': 5.5,
            'loan_term': 24
        }
        
        # Payload with invalid loan term (negative value)
        self.invalid_loan_offer_term_payload = {
            'customer': self.customer.id,
            'loan_amount': 10000.00,
            'interest_rate': 5.5,
            'loan_term': -24
        }
        
        # Payload with invalid interest rate (negative value)
        self.invalid_loan_offer_rate_payload = {
            'customer': self.customer.id,
            'loan_amount': 10000.00,
            'interest_rate': -5.5,
            'loan_term': 24
        }

        # Payload with invalid loan amount (negative value)
        self.invalid_loan_offer_amount_payload = {
            'customer': self.customer.id,
            'loan_amount': -10000.00,
            'interest_rate': 5.5,
            'loan_term': 24
        }

    # Test creating a loan offer with valid data
    def test_create_loan_offer_valid(self):
        # Send a POST request to create a new loan offer with valid data
        response = self.client.post(self.loan_offer_url, self.valid_loan_offer_payload, format='json')
        
        # Assert that the response status code is 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Parse the response data
        response_data = response.json()
        
        # Assert that the response contains an 'id' field
        self.assertIn('id', response_data)
        
        # Assert that the response contains the correct data for 'loan_amount', 'interest_rate', and 'loan_term'
        self.assertEqual(response_data['loan_amount'], '10000.00')
        self.assertEqual(response_data['interest_rate'], '5.50')
        self.assertEqual(response_data['loan_term'], 24)

    # Test creating a loan offer with invalid data (non-existent customer ID)
    def test_create_loan_offer_invalid(self):
        # Send a POST request to create a new loan offer with invalid data
        response = self.client.post(self.loan_offer_url, self.invalid_loan_offer_payload, format='json')
        
        # Assert that the response status code is 400 BAD REQUEST
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test creating a loan offer with an invalid loan term (negative value)
    def test_create_loan_offer_invalid_term(self):
        # Send a POST request to create a new loan offer with an invalid loan term
        response = self.client.post(self.loan_offer_url, self.invalid_loan_offer_term_payload, format='json')
        
        # Assert that the response status code is 400 BAD REQUEST
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Parse the response data
        response_data = response.json()
        
        # Assert that the response contains the correct error message for 'loan_term'
        self.assertIn('loan_term', response_data)
        self.assertEqual(response_data['loan_term'][0], "Loan term must be a positive value.")

    # Test creating a loan offer with an invalid interest rate (negative value)
    def test_create_loan_offer_invalid_rate(self):
        # Send a POST request to create a new loan offer with an invalid interest rate
        response = self.client.post(self.loan_offer_url, self.invalid_loan_offer_rate_payload, format='json')
        
        # Assert that the response status code is 400 BAD REQUEST
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Parse the response data
        response_data = response.json()
        
        # Assert that the response contains the correct error message for 'interest_rate'
        self.assertIn('interest_rate', response_data)
        self.assertEqual(response_data['interest_rate'][0], "Interest rate must be a positive value.")
    
    # Test creating a loan offer with an invalid loan amount (negative value)
    def test_create_loan_offer_invalid_amount(self):
        # Send a POST request to create a new loan offer with an invalid loan amount
        response = self.client.post(self.loan_offer_url, self.invalid_loan_offer_amount_payload, format='json')
        
        # Assert that the response status code is 400 BAD REQUEST
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Parse the response data
        response_data = response.json()
        
        # Assert that the response contains the correct error message for 'loan_amount'
        self.assertIn('loan_amount', response_data)
        self.assertEqual(response_data['loan_amount'][0], "Loan amount must be a positive value.")
