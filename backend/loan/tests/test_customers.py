from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from loan.models import Customer

# This class contains tests for the Customer-related API endpoints.
class CustomerTests(APITestCase):

    # The setUp method is called before each test. It sets up common test data and URLs.
    def setUp(self):
        # URL for creating a new customer
        self.customer_create_url = reverse('customer-create')
        
        # Payload with valid customer data for testing the customer creation endpoint
        self.valid_customer_payload = {
            'first_name': 'Glen',
            'last_name': 'Lohja',
            'email': 'glenlohja@example.com'
        }
        
        # Payload with invalid customer data (empty first name and last name, and invalid email)
        self.invalid_customer_payload_empty_name = {
            'first_name': '',
            'last_name': '',
            'email': 'not-an-email@example.com'
        }
        self.invalid_customer_payload_invalid_email = {
            'first_name': 'Glen',
            'last_name': 'Lohja',
            'email': 'not-an-email'
        }
        
        # Payload with duplicate email
        self.duplicate_email_payload = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'glenlohja@example.com'  # Duplicate email
        }

        # Create a customer instance directly in the database for duplicate email test
        Customer.objects.create(**self.valid_customer_payload)

    # Test creating a customer with valid data
    def test_create_customer_valid(self):
        # Send a POST request to create a new customer with valid data
        response = self.client.post(self.customer_create_url, {
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'johnsmith@example.com'
        }, format='json')
        
        # Assert that the response status code is 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Parse the response data
        response_data = response.json()
        
        # Assert that the response contains an 'id' field
        self.assertIn('id', response_data)
        
        # Assert that the response contains the correct data for 'first_name', 'last_name', and 'email'
        self.assertEqual(response_data['first_name'], 'John')
        self.assertEqual(response_data['last_name'], 'Smith')
        self.assertEqual(response_data['email'], 'johnsmith@example.com')

    # Test creating a customer with invalid data (empty first name and last name)
    def test_create_customer_empty_name(self):
        # Send a POST request to create a new customer with empty name fields
        response = self.client.post(self.customer_create_url, self.invalid_customer_payload_empty_name, format='json')
        
        # Assert that the response status code is 400 BAD REQUEST
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Parse the response data
        response_data = response.json()
        
        # Assert that the response contains the correct error message for 'first_name'
        self.assertIn('first_name', response_data)
        self.assertEqual(response_data['first_name'][0], "This field may not be blank.")
        
        # Assert that the response contains the correct error message for 'last_name'
        self.assertIn('last_name', response_data)
        self.assertEqual(response_data['last_name'][0], "This field may not be blank.")

    # Test creating a customer with an invalid email
    def test_create_customer_invalid_email(self):
        # Send a POST request to create a new customer with an invalid email
        response = self.client.post(self.customer_create_url, self.invalid_customer_payload_invalid_email, format='json')
        
        # Assert that the response status code is 400 BAD REQUEST
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Parse the response data
        response_data = response.json()
        
        # Assert that the response contains the correct error message for 'email'
        self.assertIn('email', response_data)
        self.assertEqual(response_data['email'][0], "Enter a valid email address.")

    # Test creating a customer with a duplicate email
    def test_create_customer_duplicate_email(self):
        # Send a POST request to create a new customer with a duplicate email
        response = self.client.post(self.customer_create_url, self.duplicate_email_payload, format='json')
        
        # Assert that the response status code is 400 BAD REQUEST
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Parse the response data
        response_data = response.json()
        
        # Assert that the response contains the correct error message for 'email'
        self.assertIn('email', response_data)
        self.assertEqual(response_data['email'][0], "customer with this email already exists.")

    # Test retrieving details of an existing customer with a valid ID
    def test_get_customer_details_valid(self):
        # Create a customer instance directly in the database
        customer = Customer.objects.create(first_name='John', last_name='Smith', email='johnsmith@example.com')
        
        # URL for retrieving customer details using the customer's ID
        url = reverse('customer-detail', args=[customer.id])
        
        # Send a GET request to retrieve the customer's details
        response = self.client.get(url)
        
        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Parse the response data
        response_data = response.json()
        
        # Assert that the response contains the correct data for 'first_name', 'last_name', and 'email'
        self.assertEqual(response_data['first_name'], 'John')
        self.assertEqual(response_data['last_name'], 'Smith')
        self.assertEqual(response_data['email'], 'johnsmith@example.com')

    # Test retrieving details of a customer with an invalid ID
    def test_get_customer_details_invalid(self):
        # URL for retrieving customer details using a non-existent customer ID (999)
        url = reverse('customer-detail', args=[999])
        
        # Send a GET request to retrieve the customer's details
        response = self.client.get(url)
        
        # Assert that the response status code is 404 NOT FOUND
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
