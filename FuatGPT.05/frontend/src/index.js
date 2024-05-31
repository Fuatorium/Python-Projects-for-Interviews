import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './app';

const root = document.getElementById('root');

if (root) {
  ReactDOM.createRoot(root).render(<App />);
} else {
  console.error('Root element not found');
}
