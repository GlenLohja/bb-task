/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ["./src/**/*.{js,jsx,ts,tsx}", "./public/index.html"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        customBlue: "#181c6c",
        customYellow: "#ffc30b",
        customHoverYellow: "#ffc30b",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
