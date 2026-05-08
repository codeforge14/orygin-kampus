/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './home/templates/**/*.html',
    './static/js/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        coral:    '#F44336',
        solar:    '#FFCC33',
        caraibe:  '#04D2DF',
        nature:   '#43A047',
        creative: '#9C27B0',
        orygin: {
          dark:  '#1E2A36',
          light: '#F5F5F5',
        },
      },
      fontFamily: {
        heading: ['Poppins', 'sans-serif'],
        body:    ['Nunito Sans', 'sans-serif'],
      },
      animation: {
        'float':        'float 6s ease-in-out infinite',
        'float-slow':   'float 9s ease-in-out infinite',
        'pulse-soft':   'pulse-soft 3s ease-in-out infinite',
        'slide-up':     'slideUp 0.6s ease forwards',
        'fade-in':      'fadeIn 0.8s ease forwards',
        'count-up':     'countUp 2s ease-out forwards',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%':      { transform: 'translateY(-18px)' },
        },
        'pulse-soft': {
          '0%, 100%': { opacity: '0.6' },
          '50%':      { opacity: '1' },
        },
        slideUp: {
          from: { opacity: '0', transform: 'translateY(32px)' },
          to:   { opacity: '1', transform: 'translateY(0)' },
        },
        fadeIn: {
          from: { opacity: '0' },
          to:   { opacity: '1' },
        },
      },
      backgroundImage: {
        'gradient-guyane': 'linear-gradient(135deg, #1E2A36 0%, #0d1821 100%)',
        'gradient-coral':  'linear-gradient(135deg, #F44336 0%, #c62828 100%)',
        'gradient-caraibe':'linear-gradient(135deg, #04D2DF 0%, #006064 100%)',
      },
      boxShadow: {
        'coral':    '0 8px 32px rgba(244,67,54,0.25)',
        'caraibe':  '0 8px 32px rgba(4,210,223,0.25)',
        'solar':    '0 8px 32px rgba(255,204,51,0.25)',
        'nature':   '0 8px 32px rgba(67,160,71,0.25)',
        'creative': '0 8px 32px rgba(156,39,176,0.25)',
        'card':     '0 4px 24px rgba(30,42,54,0.08)',
        'card-hover': '0 16px 48px rgba(30,42,54,0.16)',
      },
    },
  },
  plugins: [],
}
