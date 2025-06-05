# Project Title: React UI with Flask Backend

This project demonstrates a simple React frontend interacting with a Python Flask backend.

## Project Structure

```
.
├── backend/            # Flask API
│   ├── app.py          # Main Flask application
│   ├── requirements.txt# Python dependencies
│   └── test_app.py     # Backend tests
├── frontend/           # React Application
│   ├── public/
│   ├── src/
│   │   ├── App.css     # Styles for App component
│   │   ├── App.js      # Main React App component
│   │   ├── App.test.js # Tests for App component
│   │   └── ...         # Other React files
│   ├── package.json
│   └── ...             # Other frontend files
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.x
- pip (Python package installer)
- Node.js and npm (or yarn)

## Setup and Running

### Backend (Flask API)

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask development server:**
    ```bash
    python app.py
    ```
    The backend API will be running on `http://localhost:5001`.

### Frontend (React App)

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    # or if you use yarn:
    # yarn install
    ```

3.  **Run the React development server:**
    ```bash
    npm start
    # or if you use yarn:
    # yarn start
    ```
    The React application will open in your browser at `http://localhost:3000` (or another port if 3000 is busy).

## Running Tests

### Backend Tests

1.  Navigate to the root directory or the `backend` directory.
2.  Ensure backend dependencies, including any test-specific ones (though `unittest` is standard), are installed.
3.  Run the tests:
    ```bash
    python -m unittest backend/test_app.py
    # or from within the backend directory:
    # python -m unittest test_app.py
    ```

### Frontend Tests

1.  Navigate to the `frontend` directory.
2.  Ensure frontend dependencies are installed.
3.  Run the tests:
    ```bash
    npm test
    # or if you use yarn:
    # yarn test
    ```

## API Endpoints

-   `GET /api/status`: Returns the status of the backend.
-   `POST /api/submit_workflow`: Accepts JSON data (e.g., `{"data": "your_value"}`) and returns a confirmation message along with the received data.
