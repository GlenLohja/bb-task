# Loan Calculator Application

## Table of Contents

1. [Overview](#overview)
2. [Design Choices](#design-choices)
   - [Backend](#backend)
   - [Frontend](#frontend)
   - [Testing](#testing)
3. [Running the Application](#running-the-application)
   - [Clone the repository](#clone-the-repository)
   - [Backend](#backend-setup)
   - [Frontend](#frontend-setup)
4. [Running Tests](#running-tests)
   - [Backend Tests](#backend-tests)
   - [Frontend Tests](#frontend-tests)
5. [API Endpoints Documentation](#api-endpoints-documentation)
   - [Customer Endpoints](#customer-endpoints)
   - [Loan Offer Endpoints](#loan-offer-endpoints)
   - [Loan Calculator Endpoint](#loan-calculator-endpoint)
6. [Validation](#validation)
7. [Application Preview](#application-preview)

## Overview

This application consists of a Django backend and a React frontend. The backend manages customer and loan offer data and performs loan calculations. The frontend allows users to input loan details and view calculated monthly payments.

## Design Choices

### Backend

- **Framework**: Django
- **Database**: SQLite
- **API Framework**: Django REST Framework (DRF)
  - **Reason**: DRF provides powerful and flexible tools for building Web APIs. It seamlessly integrates with Django, allowing for easy serialization, validation, and routing of API endpoints.
- **Models**:
  - **Customer**: Stores customer details such as first name, last name, and email.
  - **LoanOffer**: Stores loan offer details including customer reference, loan amount, interest rate, and loan term.
- **Endpoints**:
  - `POST /api/v1/customers`: Create a new customer.
  - `GET /api/v1/customers/{id}`: Retrieve details of a customer.
  - `POST /api/v1/loanoffers`: Create a loan offer for a customer.
  - `POST /api/v1/loan-calculator`: Calculate monthly loan payments based on the loan amount, interest rate, and term.

### Frontend

- **Framework**: React
- **Styling**: Tailwind CSS
  - **Reason**: Tailwind CSS provides a highly customizable, low-level utility-first CSS framework. It allows for rapid styling without leaving the HTML, leading to faster development and a more streamlined workflow.
- **Components**:
  - **LoanCalculator**: Main component that handles input fields for loan amount, interest rate, and loan term, and displays the calculated monthly payment.
  - **InputField**: Reusable input field component with validation and error display.

### Testing

- **Backend Testing**:
  - **Framework**: Django's built-in testing framework
  - **Tools**: unittest, Django Test Client
  - **Coverage**: Tests cover models, views, serializers, and API endpoints.

- **Frontend Testing**:
  - **Framework**: Jest
  - **Tools**: React Testing Library
  - **Coverage**: Tests cover components, hooks, and API interactions.

## Running the Application

### Clone the repository:
   ```sh
   git clone https://github.com/GlenLohja/bb-task
   cd bb-task
   ```

### Backend Setup

#### Prerequisites (**Required**)

**Before you begin, ensure you have met the following requirements:**

- Python 3.x [official Python website](https://www.python.org/downloads/).
- pip (Python package installer)

#### Setup

1. Navigate to the backend directory:
   ```sh
   cd backend
   ```
2. Install the required packages:
   ```sh
   pip install -r requirements.txt
3. Apply database migrations:
   ```sh
   python manage.py migrate
   ```
4. Run the development server:
   ```sh
   python manage.py runserver
   ```

### Frontend Setup

#### Prerequisites (**Required**)

**Before you begin, ensure you have met the following requirements:**

- Node.js (v14.x and above). [official Node.js website](https://nodejs.org/).
- npm (Node package manager)
- backend must be running
  
#### Setup

**To start go back to the main directory that we cloned earlier (bb-task)**

1. Navigate to the frontend directory:
   ```sh
   cd frontend
   npm install
   ```
2. Start the development server (Keep django backend running for the calculator to work):
   ```sh
   npm start
   ```
   
The frontend application should now be running on http://localhost:3000.

## Running Tests

### Backend Tests

Django tests can be found in :  [backend/loan/tests](https://github.com/GlenLohja/bb-task/tree/main/backend/loan/tests)


1. Navigate to the backend directory:
   ```sh
   cd backend
   ```
2. Run the tests using Django's test runner
   ```sh
   python manage.py test loan/tests
   ```
### Frontend Tests

React (Jest) tests can be found in : [frontend/src/components/__tests__](https://github.com/GlenLohja/bb-task/tree/main/frontend/src/components/__tests__)

1. Navigate to the frontend directory:
   ```sh
   cd frontend
   ```
2. Run the tests using Jest
   ```sh
   npm test
   ```

## API Endpoints Documentation

### Customer Endpoints

- **Create a new customer**
  - **URL**: `POST /api/v1/customers`
  - **Request Body**:
    ```json
    {
      "first_name": "John",
      "last_name": "Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "first_name": "John",
      "last_name": "Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Retrieve details of a customer**
  - **URL**: `GET /api/v1/customers/{id}`
  - **Response**:
    ```json
    {
      "id": 1,
      "first_name": "John",
      "last_name": "Doe",
      "email": "john.doe@example.com"
    }
    ```

### Loan Offer Endpoints

- **Create a loan offer**
  - **URL**: `POST /api/v1/loanoffers`
  - **Request Body**:
    ```json
    {
      "customer": 1,
      "loan_amount": 10000.00,
      "interest_rate": 5.5,
      "loan_term": 24
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "customer": 1,
      "loan_amount": "10000.00",
      "interest_rate": "5.50",
      "loan_term": 24
    }
    ```

### Loan Calculator Endpoint

- **Calculate monthly loan payments**
  - **URL**: `POST /api/v1/loan-calculator`
  - **Request Body**:
    ```json
    {
      "loan_amount": 10000.00,
      "interest_rate": 5.5,
      "loan_term": 24
    }
    ```
  - **Response**:
    ```json
    {
      "monthly_payment": 440.96
    }
    ```

## Validation

- **Backend Validation**:
  - The backend validates that the loan amount is positive, the interest rate is non-negative, and the loan term is positive.
  - Customer email must be unique and valid.
  - Name and Last Name cannot be NULL

- **Frontend Validation**:
  - The frontend ensures that the loan amount, interest rate, and loan term are positive numbers before submitting the form.
  - Displays appropriate error messages for invalid inputs.

## Application Preview

Here’s a quick preview of the main page of the Loan Calculator Application:

![Main Page Screenshot](https://github.com/GlenLohja/bb-task/blob/main/react-page-overview.png)


