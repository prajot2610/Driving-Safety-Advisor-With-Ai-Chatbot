import { useState } from 'react';
import { Box, Container, Grid, Paper, Typography, AppBar, Toolbar } from '@mui/material';
import ChatBot from 'react-simple-chatbot';
import styled from 'styled-components';

const ChatbotContainer = styled.div`
  .rsc-container {
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }
`;

const steps = [
  {
    id: '1',
    message: 'Hello! I\'m your Driving Safety Assistant. How can I help you today?',
    trigger: '2',
  },
  {
    id: '2',
    options: [
      { value: 1, label: 'Safety Tips', trigger: '3' },
      { value: 2, label: 'Weather Driving', trigger: '4' },
      { value: 3, label: 'Emergency Guidance', trigger: '5' },
    ],
  },
  {
    id: '3',
    message: 'Here are some essential safety tips:\n1. Always wear your seatbelt\n2. Maintain safe following distance\n3. Avoid distractions while driving\n4. Regular vehicle maintenance',
    trigger: '2',
  },
  {
    id: '4',
    message: 'For safe weather driving:\n1. Reduce speed in wet conditions\n2. Use headlights in poor visibility\n3. Increase following distance\n4. Check weather forecast before long trips',
    trigger: '2',
  },
  {
    id: '5',
    message: 'In case of emergency:\n1. Pull over safely if possible\n2. Turn on hazard lights\n3. Call emergency services if needed\n4. Stay calm and assess the situation',
    trigger: '2',
  },
];

function App() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static" sx={{ backgroundColor: '#1976d2' }}>
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Driving Safety Advisor
          </Typography>
        </Toolbar>
      </AppBar>
      <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
        <Grid container spacing={3}>
          <Grid item xs={12} md={8}>
            <Paper
              sx={{
                p: 2,
                display: 'flex',
                flexDirection: 'column',
                minHeight: 240,
              }}
            >
              <Typography variant="h5" gutterBottom>
                Safety Dashboard
              </Typography>
              <Typography variant="body1" paragraph>
                Welcome to your driving safety dashboard. Here you'll find real-time safety tips,
                weather alerts, and emergency guidance. Use the chatbot assistant for personalized advice.
              </Typography>
            </Paper>
          </Grid>
          <Grid item xs={12} md={4}>
            <Paper
              sx={{
                p: 2,
                display: 'flex',
                flexDirection: 'column',
                minHeight: 240,
              }}
            >
              <Typography variant="h6" gutterBottom>
                Safety Assistant
              </Typography>
              <ChatbotContainer>
                <ChatBot
                  steps={steps}
                  headerTitle="Driving Safety Assistant"
                  floating={false}
                  style={{ width: '100%', height: '400px' }}
                />
              </ChatbotContainer>
            </Paper>
          </Grid>
        </Grid>
      </Container>
    </Box>
  );
}

export default App;
