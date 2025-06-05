import unittest
import json
from app import app # Assuming your Flask app instance is named 'app' in app.py

class BasicTests(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        # Propagate the exceptions to the test client
        self.app.testing = True

    def test_status_endpoint(self):
        # Send a GET request to the /api/status endpoint
        response = self.app.get('/api/status')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['status'], 'Backend is running!')

    def test_submit_workflow_endpoint(self):
        # Send a POST request to the /api/submit_workflow endpoint
        payload = {'data': 'test_payload'}
        response = self.app.post('/api/submit_workflow',
                                   data=json.dumps(payload),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['message'], 'Workflow submitted successfully')
        self.assertEqual(data['received_data'], payload)

if __name__ == "__main__":
    unittest.main()
