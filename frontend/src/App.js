import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [status, setStatus] = useState('');
  const [inputValue, setInputValue] = useState('');
  const [workflowResponse, setWorkflowResponse] = useState(null);

  // Fetch status from backend
  useEffect(() => {
    fetch('http://localhost:5001/api/status') // Assuming backend runs on port 5001
      .then(res => res.json())
      .then(data => setStatus(data.status))
      .catch(err => {
        console.error("Error fetching status:", err);
        setStatus('Error fetching status. Is the backend running?');
      });
  }, []);

  // Handle workflow submission
  const handleSubmitWorkflow = (e) => {
    e.preventDefault();
    setWorkflowResponse(null); // Clear previous response
    fetch('http://localhost:5001/api/submit_workflow', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ data: inputValue }),
    })
      .then(res => res.json())
      .then(data => setWorkflowResponse(data))
      .catch(err => {
        console.error("Error submitting workflow:", err);
        setWorkflowResponse({ message: 'Error submitting workflow.' });
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>React Frontend</h1>
      </header>
      <section>
        <h2>Backend Status</h2>
        <p>{status}</p>
      </section>
      <section>
        <h2>Submit Workflow</h2>
        <form onSubmit={handleSubmitWorkflow}>
          <div>
            <label htmlFor="workflowInput">Enter data: </label>
            <input
              type="text"
              id="workflowInput"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
            />
          </div>
          <button type="submit">Submit</button>
        </form>
        {workflowResponse && (
          <div>
            <h3>Workflow Submission Response:</h3>
            <pre>{JSON.stringify(workflowResponse, null, 2)}</pre>
          </div>
        )}
      </section>
    </div>
  );
}

export default App;
