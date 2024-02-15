# app.py

from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

# Mock endpoint data
mock_endpoints = [
    {"id": 1, "hostname": "endpoint1.example.com", "status": "Online"},
    {"id": 2, "hostname": "endpoint2.example.com", "status": "Offline"},
    {"id": 3, "hostname": "endpoint3.example.com", "status": "Online"},
]

@app.route('/')
def index():
    return render_template('index.html', endpoints=mock_endpoints)

@app.route('/endpoint/<int:endpoint_id>')
def endpoint_detail(endpoint_id):
    # Fetch endpoint details from a hypothetical management system or API
    endpoint = next((endpoint for endpoint in mock_endpoints if endpoint['id'] == endpoint_id), None)
    if endpoint:
        return render_template('endpoint_detail.html', endpoint=endpoint)
    else:
        return "Endpoint not found.", 404

@app.route('/manage', methods=['POST'])
def manage():
    if request.method == 'POST':
        endpoint_id = request.form['endpoint_id']
        action = request.form['action']
        # Perform management action (e.g., deploy agent, update policy) on the endpoint
        # This could involve making API calls to an endpoint management system
        return redirect(url_for('endpoint_detail', endpoint_id=int(endpoint_id)))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
