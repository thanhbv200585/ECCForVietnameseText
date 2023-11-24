# Elliptic Curve Cryptosystem with the Symmetric Key for Vietnamese Text Encryption and Decryption Programme

In this project, we implement an algorithm for Vietnamese text encryption and decryption based on he basic idea of Elliptic curve cryptography (ECC) 

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [References](#references)

## Project Description

The project describes the basic idea of Elliptic curve cryptography (ECC). Elliptic curve arithmetic can be used to develop Elliptic curve coding schemes, including key exchange, encryption, and digital signature. The main attraction of Elliptic curve cryptography compared to RSA is that it provides equivalent security for a smaller key size, which reduces
processing costs. To encode the Vietnamese text, we are based on the sound of Vietnamese characters to make a table of thesecharacters’ order. We are also based on the algorithm to create the data sequence as the basis of building an encryption algorithm by using Elliptic curves on finite fields with symmetric keys to encrypt this Vietnamese text

## Features

- Encryption: the function will be called to encrypt the text
- Decryption: the function will be called to decrypt the text
- EllipticCurve: the class will represent a curve using to encrypt and decrypt the text

## Installation

### Prerequisites

Before getting started, ensure that you have the following prerequisites installed:

- Node.js and npm: Follow the [official Node.js installation guide](https://nodejs.org/) to install Node.js and npm on your machine.
- [Docker](https://docs.docker.com/engine/install/)
### Backend

1. Clone the repository.
2. Navigate to the backend directory: `cd backend`.
3. Build the Docker image using the provided Dockerfile: `docker build -t backend-image .`
4. Run the Docker container using the built image: `docker run -p 5000:5000 --network host backend-image`

### Frontend

1. Clone the repository.
2. Navigate to the frontend directory: `cd frontend`.
3. Install the required dependencies: `npm install`.
4. Start the frontend development server: `npm start`.


## References

- [Proposing an Elliptic Curve Cryptosystem with the Symmetric Key for Vietnamese Text Encryption and Decryption](https://eprints.uet.vnu.edu.vn/eprints/id/eprint/4028/1/Final_ijatcse246932020.pdf)
- [Elliptic Curve Cryptography (ECC)](https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc)