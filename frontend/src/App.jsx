import EncryptionForm from './components/EncryptionForm';
import DecryptionForm from './components/DecryptionForm';
import './App.css'; // Import your CSS file

const Header = () => {
  return (
    <div className="text-center my-8">
      <h1 className="text-3xl font-bold text-gray-800">
        Elliptic Curve Cryptosystem with the Symmetric Key
        for Vietnamese Text Encryption and Decryption Programme
      </h1>
    </div>
  );
};

function App() {
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-800">
      <Header />
      <div className="flex space-x-8">
        <EncryptionForm />
        <DecryptionForm />
      </div>
    </div>
  );
}

export default App;
