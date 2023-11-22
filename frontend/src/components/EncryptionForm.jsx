// src/components/EncryptionForm.js
import { useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS

const EncryptionForm = () => {
  const [a, setA] = useState('');
  const [b, setB] = useState('');
  const [p, setP] = useState('');
  const [key, setKey] = useState('');
  const [input, setInput] = useState('');
  const [encryptResult, setEncryptResult] = useState('');

  const handleEncrypt = async () => {
    try {
      const response = await axios.post('http://localhost:5000/encrypt', {
        a,
        b,
        p,
        input_key: key,
        plain_text: input,
      });
      setEncryptResult(response.data.encrypted_data);
    } catch (error) {
      console.error('Error encrypting data:', error);
      // Handle error state here
    }
  };



  return (
    <div className="w-50 container my-4">
      <div className="card p-4">
        <h2 className="text-2xl font-bold mb-4 text-center text-dark">Encryption Form</h2>
        <div className="row g-2 flex ">
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
              placeholder="Enter plain text"
              className="form-control"
            />
          </div>
        </div>
        <button
          onClick={handleEncrypt}
          className="btn btn-primary mt-3 w-100"
        >
          Encrypt
        </button>
        <p className="mt-3 text-secondary text-center">
          Encrypted Result: 
        </p>
        <span className="font-weight-bold">{encryptResult}</span>
      </div>
    </div>
  );
};

export default EncryptionForm;
