import React from 'react';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { AppBar, Toolbar, Typography, Container, Paper } from '@mui/material';

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <div className="App">
        <AppBar position="static">
          <Toolbar>
            <Typography variant="h6">
              Smart Surveillance System
            </Typography>
          </Toolbar>
        </AppBar>
        <Container style={{ marginTop: '2rem' }}>
          <Paper elevation={3} style={{ padding: '2rem' }}>
            <Typography variant="h4" gutterBottom>
              Live Video Feed
            </Typography>
            <img src="http://localhost:5000/video_feed" alt="Video Feed" width="100%"/>
          </Paper>
        </Container>
      </div>
    </ThemeProvider>
  );
}

export default App;
