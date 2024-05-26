import React from "react";
import LoanCalculator from "./components/Calculator";
import Header from "./components/Header/Header";

function App() {
  return (
    <div>
      <Header />
      <main>
        <LoanCalculator />
      </main>
    </div>
  );
}

export default App;
