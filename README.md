# Driving Safety Advisor

A modern web application that provides real-time driving safety advice through an AI-powered chatbot interface. The application includes comprehensive safety tips and emergency response guidelines.

## Features

- Interactive AI Chatbot for driving safety queries
- Comprehensive driving safety tips
- Emergency response guidelines
- Modern, responsive user interface

## Prerequisites

Before you begin, ensure you have installed:
- [Node.js](://nhttpsodejs.org/) (version 14.0.0 or higher)
- [npm](https://www.npmjs.com/) (usually comes with Node.js)

## Installation

1. Clone the repository or download the source code

2. Install the required dependencies:
```bash
npm install
```

3. Install the following specific dependencies if the above command fails:
```bash
npm install react react-dom react-router-dom @mui/material @emotion/react @emotion/styled @mui/icons-material
npm install --save-dev @vitejs/plugin-react vite @types/react @types/react-dom eslint eslint-plugin-react eslint-plugin-react-hooks eslint-plugin-react-refresh
```

## Development

To start the development server:

```bash
npm run dev
```

The application will be available at `http://localhost:3000`

## Building for Production

To create a production build:

```bash
npm run build
```

To preview the production build:

```bash
npm run preview
```

## Project Structure

```
├── src/
│   ├── components/
│   │   ├── ChatInterface.jsx    # AI Chatbot interface
│   │   ├── EmergencyGuide.jsx   # Emergency response guidelines
│   │   ├── Navbar.jsx           # Navigation component
│   │   └── SafetyTips.jsx       # Driving safety tips
│   ├── App.jsx                  # Main application component
│   ├── main.jsx                 # Application entry point
│   ├── theme.js                 # Material-UI theme configuration
│   └── index.css               # Global styles
├── index.html                   # HTML entry point
├── package.json                 # Project dependencies and scripts
└── vite.config.js              # Vite configuration
```

## Technologies Used

- React
- Material-UI
- React Router
- Vite
- ESLint
