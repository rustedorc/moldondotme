/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: [
    "./templates/**/*.html",
    // "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: { fontFamily: {
      'custom': ['"Helvetica Neue"', 'Arial', 'sans-serif']
    },
    colors: {
      'custom-dark': '#1a202c',
      'custom-light': '#718096',
    }},
  },
  plugins: [
    // require("flowbite/plugin")
  ],
}

