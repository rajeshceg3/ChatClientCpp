import { render, screen, waitFor } from '@testing-library/react';
import App from './App';

// Mock the fetch function
global.fetch = jest.fn((url) => {
  if (url.endsWith('/api/status')) {
    return Promise.resolve({
      json: () => Promise.resolve({ status: 'Backend is running!' }),
    });
  }
  // You can add more mocks for other endpoints if needed for more complex tests
  return Promise.reject(new Error('not found'));
});

test('renders the header', () => {
  render(<App />);
  const headerElement = screen.getByText(/React Frontend/i);
  expect(headerElement).toBeInTheDocument();
});

test('fetches and displays backend status', async () => {
  render(<App />);
  // Wait for the status to be displayed
  // Using findByText because the status is fetched asynchronously
  const statusElement = await screen.findByText(/Backend is running!/i);
  expect(statusElement).toBeInTheDocument();
});

test('renders the submit workflow form', () => {
  render(<App />);
  const inputLabelElement = screen.getByLabelText(/Enter data:/i);
  expect(inputLabelElement).toBeInTheDocument();
  const submitButtonElement = screen.getByRole('button', { name: /Submit/i });
  expect(submitButtonElement).toBeInTheDocument();
});

// To run this test, you would typically use `npm test` in the `frontend` directory.
// This subtask is just about creating/modifying the test file.
