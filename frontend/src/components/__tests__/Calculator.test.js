import {
  render,
  screen,
  fireEvent,
  cleanup,
  waitFor,
} from "@testing-library/react";
import LoanCalculator from "../Calculator";

// Helper function to fill out the form
const fillForm = (loanAmount, interestRate, loanTerm) => {
  fireEvent.change(screen.getByPlaceholderText("Enter your loan amount"), {
    target: { value: loanAmount },
  });
  fireEvent.change(screen.getByPlaceholderText("Enter interest rate"), {
    target: { value: interestRate },
  });
  fireEvent.change(screen.getByPlaceholderText("Enter loan term"), {
    target: { value: loanTerm },
  });
};

// Helper function to click the calculate button
const clickCalculate = () => {
  fireEvent.click(screen.getByRole("button", { name: /calculate/i }));
};

afterEach(() => {
  cleanup();
  jest.resetAllMocks();
});

test("Should render the Calculator Component", () => {
  render(<LoanCalculator />);
  const calculatorElement = screen.getByTestId("calculator-1");
  expect(calculatorElement).toBeInTheDocument();
  expect(calculatorElement).toHaveTextContent("Calculate Your Monthly Payment");
});

test("Should show validation errors for empty fields", () => {
  render(<LoanCalculator />);
  clickCalculate();
  expect(screen.getByText("Loan amount is required.")).toBeInTheDocument();
  expect(screen.getByText("Interest rate is required.")).toBeInTheDocument();
  expect(screen.getByText("Loan term is required.")).toBeInTheDocument();
});

test("Should show validation errors for invalid input values", () => {
  render(<LoanCalculator />);
  fillForm("-1000", "0", "12.5");
  clickCalculate();
  expect(
    screen.getByText("Loan amount must be a positive number.")
  ).toBeInTheDocument();
  expect(
    screen.getByText("Interest rate must be a positive number.")
  ).toBeInTheDocument();
  expect(
    screen.getByText("Loan term must be a whole number.")
  ).toBeInTheDocument();
});

test("Should calculate monthly payment when inputs are valid", async () => {
  render(<LoanCalculator />);

  // Mocking the fetch API response
  global.fetch = jest.fn(() =>
    Promise.resolve({
      ok: true,
      json: () => Promise.resolve({ monthly_payment: 188.71 }),
    })
  );

  fillForm("10000", "5", "60");
  clickCalculate();

  await waitFor(() =>
    expect(
      screen.getByText(/Your Monthly Payment Is: \$188.71/)
    ).toBeInTheDocument()
  );
});

test("Should display error message when API request fails", async () => {
  render(<LoanCalculator />);

  // Mocking the fetch API to return an error
  global.fetch = jest.fn(() =>
    Promise.resolve({
      ok: false,
    })
  );

  // Mock console.error to prevent actual error logging during the test
  jest.spyOn(console, "error").mockImplementation(() => {});

  fillForm("10000", "5", "60");
  clickCalculate();

  await waitFor(() =>
    expect(
      screen.getByText(/Failed to calculate loan payment. Please try again./)
    ).toBeInTheDocument()
  );
});

test("Should make correct API call with the right parameters", async () => {
  render(<LoanCalculator />);

  global.fetch = jest.fn(() =>
    Promise.resolve({
      ok: true,
      json: () => Promise.resolve({ monthly_payment: 188.71 }),
    })
  );

  fillForm("10000", "5", "60");
  clickCalculate();

  await waitFor(() => {
    expect(global.fetch).toHaveBeenCalledTimes(1);
    expect(global.fetch).toHaveBeenCalledWith(
      "http://127.0.0.1:8000/api/v1/loan-calculator",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          loan_amount: 10000,
          interest_rate: 5,
          loan_term: 60,
        }),
      }
    );
  });
});
