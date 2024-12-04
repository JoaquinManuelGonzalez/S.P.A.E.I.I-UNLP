/** @type {import('tailwindcss').Config} */
import flowbite from 'flowbite/plugin';

export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'], // No 'purge'
  theme: {
    extend: {},
  },
  plugins: [
    flowbite,
  ],
}