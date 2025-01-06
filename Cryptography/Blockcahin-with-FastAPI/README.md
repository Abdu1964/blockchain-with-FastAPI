# Blockchain FastAPI & UTXO Blockchain Implementation

## Overview
This project demonstrates two blockchain implementations:

1. **Blockchain FastAPI Implementation** - A simple blockchain with FastAPI endpoints for mining blocks, accepting transactions, adding blocks, and fetching the blockchain.
2. **UTXO Blockchain Implementation** - A blockchain using the Unspent Transaction Output (UTXO) model to handle transactions, including UTXO generation, signing, verification, and processing.

## Blockchain FastAPI Implementation

### Objective
The goal is to implement FastAPI endpoints to manage blockchain functionalities:

- Mining a new block.
- Accepting new transactions.
- Adding received blocks to the chain.
- Fetching the current blockchain.

### Requirements
- Python 3.x
- FastAPI and Uvicorn for serving the application.

### Endpoints:

#### `/mine_block`
- **Method**: POST
- **Response**: Success or error message with mined block data.

#### `/new_transaction`
- Accepts transaction data (sender, receiver, amount, input UTXOs, output UTXOs, signature) and adds it to a list of pending transactions.
- **Method**: POST
- **Body**:
    ```json
    {
      "sender": "sender_address",
      "receiver": "receiver_address",
      "amount": 10,
      "input_utxos": ["utxo1", "utxo2"],
      "output_utxos": ["utxo3", "utxo4"],
      "signature": "transaction_signature"
    }
    ```
- **Response**: Success message.

#### `/add_block`
- Accepts a block and validates it before appending it to the chain.
- **Method**: POST
- **Body**:
    ```json
    {
      "index": 1,
      "transactions": [{"sender": "sender_address", "receiver": "receiver_address", "amount": 10}],
      "previous_hash": "previous_hash_value",
      "proof": 123456,
      "timestamp": 1638246823
    }
    ```
- **Response**: Success or error message.

#### `/chain`
- Returns the current blockchain.
- **Method**: GET
- **Response**: List of all blocks in the blockchain.

### Blockchain Functions:
- **Mining**: Mines new blocks via a proof-of-work algorithm.
- **Transactions**: Adds pending transactions to a mined block.
- **Block Validation**: Ensures blocks are valid before adding them to the chain.

### How to Run:

#### Install dependencies:
```bash
pip install fastapi uvicorn
Run the FastAPI app:

uvicorn fastapi:app --reload
Open the browser and go to http://127.0.0.1:8000/docs to interact with the API using Swagger UI.
```

### Example Usage:

- **Mine a Block**:  
  `POST /mine_block`

- **Add a New Transaction**:  
  `POST /new_transaction` with transaction data.

- **Add a Block**:  
  `POST /add_block` with block data.

- **Get the Blockchain**:  
  `GET /chain` to retrieve the current blockchain.

## Code Explanation:

- **blockchain.py**: Contains the blockchain logic (block creation, mining, transactions).
- **fastapi.py**: Defines FastAPI endpoints for interacting with the blockchain.

## Features and Enhancements:

- **Proof-of-Work**: Simple proof-of-work where the hash of the proof must start with a "0".
- **Transaction Handling**: Transactions are added to the chain once mined.
- **Block Validation**: Ensures blocks are properly linked.

## Future Enhancements:

- **Consensus Mechanism**: Implement a more advanced algorithm for block validation across multiple nodes.
- **Blockchain UI**: Create an interface to visualize the blockchain.
- **Transaction Pool**: Manage pending transactions with a more complex system.
