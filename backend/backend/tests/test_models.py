from django.test import TestCase
from backend.models import Customer, LoanOffer

# This class contains tests for the Customer model.
class CustomerModelTests(TestCase):

    # The setUp method is called before each test. It sets up common test data.
    def setUp(self):
        # Create a test customer in the database
        self.customer = Customer.objects.create(
            first_name='Glen',
            last_name='Lohja',
            email='glenlohja@example.com'
        )

    # Test the __str__ method of the Customer model
    def test_customer_str(self):
        # Assert that the string representation of the customer is correct
        self.assertEqual(str(self.customer), 'Glen Lohja')

# This class contains tests for the LoanOffer model.
class LoanOfferModelTests(TestCase):

    # The setUp method is called before each test. It sets up common test data.
    def setUp(self):
        # Create a test customer in the database
        self.customer = Customer.objects.create(
            first_name='Glen',
            last_name='Lohja',
            email='glenlohja@example.com'
        )
        
        # Create a test loan offer associated with the test customer
        self.loan_offer = LoanOffer.objects.create(
            customer=self.customer,
            loan_amount=10000.00,
            interest_rate=5.5,
            loan_term=24
        )

    # Test the __str__ method of the LoanOffer model
    def test_loan_offer_str(self):
        # Assert that the string representation of the loan offer is correct
        self.assertEqual(str(self.loan_offer), f'Loan for {self.customer} - Amount: 10000.0')
