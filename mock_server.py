from flask import Flask, request, jsonify, make_response
from pymongo import MongoClient
from bson.json_util import dumps
import os

app = Flask(__name__)

MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
DB_NAME = os.environ.get('MONGO_DB', 'mockserver')
COLLECTION_NAME = 'mocks'

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
mocks_collection = db[COLLECTION_NAME]

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def mock_handler(path):
    full_path = '/' + path
    method = request.method.upper()

    mock = mocks_collection.find_one({'uri': full_path, 'method': method})

    if mock:
        response_body = mock.get('response', '{}')
        status_code = mock.get('statusCode', 200)

        return make_response(response_body, status_code, {'Content-Type': 'application/json'})
    else:
        return make_response(jsonify({'error': 'Mock not found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
