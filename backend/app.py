import sys
sys.path.append("..")
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS module
from utils import decryption, encryption,  generate_mapping_table
from ECC import EllipticCurve
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/encrypt', methods=['POST'])
def encrypt():
    # Perform encryption logic on the data
    data = request.get_json()
    a = data['a']
    b = data['b']
    p = data['p']
    input_key = data['input_key']
    plain_text = data['plain_text']
    
    curve = EllipticCurve(a, b, p)
    mapping_table = generate_mapping_table(curve)

    try:
        encrypted_data = encryption(mapping_table, plain_text, input_key)
        return {'encrypted_data': encrypted_data}
    except ValueError:
        response = jsonify({'error': 'The triple (a, b, p) is not suitable'})
        response.status_code = 500
        return response

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    a = data['a']
    b = data['b']
    p = data['p']
    input_key = data['input_key']
    cipher_text = data['cipher_text']

    curve = EllipticCurve(a, b, p)
    mapping_table = generate_mapping_table(curve)

    try:
        encrypted_data = decryption(mapping_table, cipher_text, input_key)
        return {'decrypted_data': encrypted_data}
    except ValueError:
        response = jsonify({'error': 'The triple (a, b, p) is not suitable'})
        response.status_code = 500
        return response

if __name__ == '__main__':
    app.run()