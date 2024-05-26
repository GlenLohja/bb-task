import React, { useState } from "react";
import InputField from "./InputField";
import reactImg from "../assets/bb-main.webp";

const LoanCalculator = () => {
  const [formData, setFormData] = useState({
    loanAmount: "",
    interestRate: "",
    loanTerm: "",
  });
  const [errors, setErrors] = useState({});
  const [monthlyPayment, setMonthlyPayment] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
    setErrors({
      ...errors,
      [e.target.name]: "",
    });
  };

  const validateInputs = () => {
    const { loanAmount, interestRate, loanTerm } = formData;
    const newErrors = {};
    setMonthlyPayment(null);

    if (!loanAmount) {
      newErrors.loanAmount = "Loan amount is required.";
    } else if (isNaN(loanAmount) || parseFloat(loanAmount) <= 0) {
      newErrors.loanAmount = "Loan amount must be a positive number.";
    }

    if (!interestRate) {
      newErrors.interestRate = "Interest rate is required.";
    } else if (isNaN(interestRate) || parseFloat(interestRate) <= 0) {
      newErrors.interestRate = "Interest rate must be a positive number.";
    }

    if (!loanTerm) {
      newErrors.loanTerm = "Loan term is required.";
    } else if (isNaN(loanTerm) || parseInt(loanTerm, 10) <= 0) {
      newErrors.loanTerm = "Loan term must be a positive number.";
    } else if (!Number.isInteger(parseFloat(loanTerm))) {
      newErrors.loanTerm = "Loan term must be a whole number.";
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleCalculate = async () => {
    if (!validateInputs()) {
      return;
    }

    setLoading(true);
    setError("");
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/v1/loan-calculator",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            loan_amount: parseFloat(formData.loanAmount),
            interest_rate: parseFloat(formData.interestRate),
            loan_term: parseInt(formData.loanTerm, 10),
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        setMonthlyPayment(null);
        const newErrors = {};
        if (data.loan_amount) {
          newErrors.loanAmount = data.loan_amount;
        }
        if (data.interest_rate) {
          newErrors.interestRate = data.interest_rate;
        }
        if (data.loan_term) {
          newErrors.loanTerm = data.loan_term;
        }
        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
      }

      setMonthlyPayment(data.monthly_payment);
    } catch (error) {
      console.error("Error calculating loan payment", error);
      setError("Failed to calculate loan payment. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section
      data-testid="calculator-1"
      className="py-5 sm:pt-16 sm:pb-1 lg:py-10"
    >
      <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row items-center justify-center mx-8 md:mt-10">
          <div className="overflow-hidden bg-white rounded-md w-full md:w-1/2 md:h-[600px]">
            <div className="mx-7 pt-5 text-left">
              <h2 className="text-2xl font-bold leading-tight text-customBlue sm:text-4xl lg:text-3xl">
                Calculate Your Monthly Payment
              </h2>
            </div>
            <div className="px-4 py-6 sm:px-8 sm:py-7">
              <div className="space-y-5">
                <InputField
                  label="Loan Amount"
                  name="loanAmount"
                  type="number"
                  placeholder="Enter your loan amount"
                  value={formData.loanAmount}
                  onChange={handleChange}
                  error={errors.loanAmount}
                  icon="dollar-sign"
                />
                <InputField
                  label="Interest Rate (%)"
                  name="interestRate"
                  type="number"
                  placeholder="Enter interest rate"
                  value={formData.interestRate}
                  onChange={handleChange}
                  error={errors.interestRate}
                  icon="percent"
                />
                <InputField
                  label="Loan Term (months)"
                  name="loanTerm"
                  type="number"
                  placeholder="Enter loan term"
                  value={formData.loanTerm}
                  onChange={handleChange}
                  error={errors.loanTerm}
                  icon="calendar-alt"
                />
                <div>
                  <button
                    onClick={handleCalculate}
                    disabled={loading}
                    data-testid="calculate-button"
                    className="inline-flex items-center justify-center w-full px-4 py-4 text-base font-semibold text-white transition-all duration-200 bg-customBlue border border-transparent rounded-md focus:outline-none hover:bg-blue-900 focus:bg-blue-900"
                  >
                    {loading ? "Calculating..." : "Calculate"}
                  </button>
                </div>
                <div style={{ height: "24px" }}>
                  {error && <div className="text-red-500">{error}</div>}
                  {monthlyPayment !== null && !error && (
                    <div className="text-1xl font-bold leading-tight text-lime-500">
                      <h2>Your Monthly Payment Is: ${monthlyPayment}</h2>
                    </div>
                  )}
                </div>
              </div>
            </div>
          </div>
          <div className="mb-12 lg:pl-11 xl:pl-12 2xl:pl-12 md:ml-10 md:w-2/5">
            <img src={reactImg} alt="Loan image" className="rounded-md" />
          </div>
        </div>
      </div>
    </section>
  );
};

export default LoanCalculator;
