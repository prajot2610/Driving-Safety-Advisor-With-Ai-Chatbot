# Driving Safety Advisor

A modern web application designed to enhance driving safety through real-time advice and interactive assistance.

## Features

- **Safety Dashboard**: Real-time display of safety tips, weather alerts, and emergency guidance
- **Interactive Chatbot**: AI-powered driving safety assistant for personalized advice
- **Modern UI**: Clean and responsive interface built with Material-UI components
- **Real-time Updates**: Instant access to safety-related information

## Technology Stack

- **Frontend Framework**: React 19
- **UI Components**: Material-UI (MUI) v7
- **Chatbot Integration**: react-simple-chatbot
- **Build Tool**: Vite 6
- **Styling**: Emotion and styled-components

## Getting Started

### Prerequisites

- Node.js (Latest LTS version recommended)
- npm (comes with Node.js)

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   ```

### Development

To start the development server:

```bash
npm run dev
```

The application will be available at `http://localhost:5173`

### Building for Production

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
│   ├── assets/        # Static assets
│   ├── App.jsx        # Main application component
│   ├── App.css        # Application styles
│   ├── main.jsx       # Application entry point
│   └── index.css      # Global styles
├── public/            # Public static files
└── vite.config.js     # Vite configuration
```

## Features Description

### Safety Dashboard
The main dashboard provides users with:
- Real-time safety tips
- Weather alerts
- Emergency guidance
- Interactive safety information

### Chatbot Assistant
An AI-powered chatbot that offers:
- Personalized driving advice
- Safety recommendations
- Emergency response guidance
- Interactive safety consultations

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
