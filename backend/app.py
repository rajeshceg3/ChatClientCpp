from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({'status': 'Backend is running!'})

@app.route('/api/submit_workflow', methods=['POST'])
def submit_workflow():
    data = request.get_json()
    # In a real application, you would process the data here
    # For this placeholder, we'll just echo it back with a message
    return jsonify({'message': 'Workflow submitted successfully', 'received_data': data})

if __name__ == '__main__':
    app.run(debug=True, port=5001) # Changed port to 5001
