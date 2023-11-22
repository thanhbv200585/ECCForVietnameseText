// src/components/DecryptionForm.js
import { useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS

const DecryptionForm = () => {
  const [a, setA] = useState('');
  const [b, setB] = useState('');
  const [p, setP] = useState('');
  const [key, setKey] = useState('');
  const [input, setInput] = useState('');
  const [decryptedResult, setDecryptResult] = useState('');

  const handleDecrypt = async () => {
    try {
      const response = await axios.post('http://localhost:5000/decrypt', {
        a,
        b,
        p,
        input_key: key,
        cipher_text: input,
      });
      console.log(response.data);
      setDecryptResult(response.data.decrypted_data);
    } catch (error) {
      console.error('Error decrypting data:', error);
      // Handle error state here
    }
  };

  return (
    <div className="container my-4 w-50">
      <div className="card p-4">
        <h2 className="text-2xl font-bold mb-4 text-center text-dark">Decryption Form</h2>
        <div className="row g-2">
          <div className="col-md-6">
            <input
              type="number"
              value={a}
              onChange={(e) => setA(e.target.value)}
              placeholder="Enter a"
              className="form-control"
            />
          </div>
          <div className="col-md-6">
            <input
              type="number"
              value={b}
              onChange={(e) => setB(e.target.value)}
              placeholder="Enter b"
              className="form-control"
            />
          </div>
          <div className="col-md-6">
            <input
              type="number"
              value={p}
              onChange={(e) => setP(e.target.value)}
              placeholder="Enter p"
              className="form-control"
            />
          </div>
          <div className="col-md-6">
            <input
              type="number"
              value={key}
              onChange={(e) => setKey(e.target.value)}
              placeholder="Enter key"
              className="form-control"
            />
          </div>
          <div className="col-md-12">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Enter cipher text"
              className="form-control"
            />
          </div>
        </div>
        <button
          onClick={handleDecrypt}
          className="btn btn-success mt-3 w-100"
        >
          Decrypt
        </button>
        <p className="mt-3 text-secondary text-center">
          Decrypted Result: 
        </p>
        <span className="font-weight-bold">{decryptedResult}</span>
      </div>
    </div>
  );
};

export default DecryptionForm;
