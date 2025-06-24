from flask import Flask, request, jsonify

app = Flask(__name__)

# GET endpoint that returns a greeting
#Testing curl http://127.0.0.1:5001/api/greet
@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify({'message': 'Hello from the REST API!'})

# POST endpoint that echoes back received JSON data
# Testing curl -X POST http://127.0.0.1:5001/api/echo -H "Content-Type: application/json" -d '{"name": "Alice", "age": 7}'
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({'you_sent': data})

# PUT endpoint that simulates updating data
# Testing curl -X PUT http://127.0.0.1:5001/api/update -H "Content-Type: application/json" -d '{"name": "Bob", "age": 10}'
@app.route('/api/update', methods=['PUT'])
def update():
    data = request.get_json()
    return jsonify({'message': 'PUT request received', 'updated_data': data})

# PATCH endpoint that simulates partial update
#Testing curl -X PATCH http://127.0.0.1:5001/api/patch -H "Content-Type: application/json" -d '{"age": 11}'
@app.route('/api/patch', methods=['PATCH'])
def patch():
    data = request.get_json()
    return jsonify({'message': 'PATCH request received', 'patched_data': data})

# DELETE endpoint that simulates deleting data
#Testing curl -X DELETE http://127.0.0.1:5001/api/delete
@app.route('/api/delete', methods=['DELETE'])
def delete():
    return jsonify({'message': 'DELETE request received'})

# OPTIONS endpoint that returns allowed methods
# Testing curl -X OPTIONS http://127.0.0.1:5001/api/options
@app.route('/api/options', methods=['OPTIONS'])
def options():
    return jsonify({'message': 'OPTIONS request received', 'allowed_methods': ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS', 'HEAD']})

# HEAD endpoint that returns headers only (no body)
# Testing curl -I -X HEAD http://127.0.0.1:5001/api/head
@app.route('/api/head', methods=['HEAD'])
def head():
    return ('', 200, {'X-Example-Header': 'Value'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
