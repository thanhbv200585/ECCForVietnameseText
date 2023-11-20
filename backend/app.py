import sys
sys.path.append("..")
from flask import Flask, request
from utils import decryption, encryption

app = Flask(__name__)


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
    n = data['n']
    input_key = data['input_key']
    plain_text = data['plain_text']
    print("a: ", a, "b: ", b, "n: ", n,"input_key: ", input_key, "plain_text: ", plain_text)
    encrypted_data = encryption("encrypted")
    return {'encrypted_data': encrypted_data}

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    a = data['a']
    b = data['b']
    n = data['n']
    input_key = data['input_key']
    cipher_text = data['cipher_text']

    print("a: ", a, "b: ", b, "n: ", n,"input_key: ", input_key, "Cipher_text: ", cipher_text)

    decrypted_data = decrypt_function("decrypted")
    return {'decrypted_data': decrypted_data}

def encrypt_function(data):
    return data

def decrypt_function(data):
    return data

if __name__ == '__main__':
    app.run()