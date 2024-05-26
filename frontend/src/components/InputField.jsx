import React from "react";
import PropTypes from "prop-types";

const InputField = ({
  label,
  name,
  type,
  placeholder,
  value,
  onChange,
  error,
  icon,
}) => (
  <div>
    <label className="text-base font-medium text-gray-900">{label}</label>
    <div className="mt-2.5 relative text-gray-400 focus-within:text-gray-600">
      <div className="absolute top-5 left-0 flex items-center pl-4 pointer-events-none">
        <i className={`fas fa-${icon} w-5 h-5`}></i>
      </div>
      <input
        type={type}
        name={name}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        className={`block w-full py-4 pl-10 pr-4 text-black placeholder-gray-500 transition-all duration-200 bg-white border border-gray-200 rounded-md focus:outline-none focus:border-blue-600 caret-blue-600 ${
          error ? "border-red-500" : ""
        }`}
      />
      {error && <div style={{ color: "red" }}>{error}</div>}
    </div>
  </div>
);

InputField.propTypes = {
  label: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  type: PropTypes.string.isRequired,
  placeholder: PropTypes.string.isRequired,
  value: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
  onChange: PropTypes.func.isRequired,
  error: PropTypes.string,
  icon: PropTypes.string.isRequired,
};

export default InputField;
