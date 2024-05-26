from rest_framework import serializers
from .models import Customer, LoanOffer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class LoanOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanOffer
        fields = '__all__'

    # custom validator to check if loan term is positive
    def validate_loan_term(self, value):
        if value <= 0:
            raise serializers.ValidationError("Loan term must be a positive value.")
        return value

    # custom validator to check if interest rate is positive
    def validate_interest_rate(self, value):
        if value <= 0:
            raise serializers.ValidationError("Interest rate must be a positive value.")
        return value

    # custom validator to check if loan amount is positive
    def validate_loan_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Loan amount must be a positive value.")
        return value