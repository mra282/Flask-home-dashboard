const path = require('path');

/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    "../templates/**/*.{html,htm}",
    path.join(__dirname, "../Blueprints/**/*.html"),
  ],
  theme: {
    extend: {
    },
  },
  variants: {
    extend: {
      backgroundColor: ['dark'],
      textColor: ['dark'],
    },
  },
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
    require('postcss-preset-env')({
      stage: 3,
      features: {
        'nesting-rules': true
      }
    }),
  ],
}