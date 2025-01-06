
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
pip install -r requirements.txt
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


# UTXO Blockchain Implementation

## Objective
The goal of this section is to demonstrate how a blockchain using the Unspent Transaction Output (UTXO) model can be implemented for handling transactions. It provides functionality for creating UTXOs, signing and verifying transactions, and processing transactions between users.

## Requirements
- **Python 3.8 or higher**
- **cryptography** package for cryptographic operations (can be installed via `pip install cryptography`)

## Features
- **UTXO Management**
  - Generates UTXOs (Unspent Transaction Outputs) for recipients.
  - Tracks UTXOs in a dictionary (`utxo_set`).
  
- **Transaction Signing and Verification**
  - Creates and signs transactions using elliptic curve cryptography (ECC).
  - Verifies transaction signatures to ensure integrity and authenticity.
  
- **Blockchain Transaction Processing**
  - Transfers funds between users, updates the UTXO set, and manages balances.
  - Supports basic transaction flow (spending UTXOs and generating new ones).
  
- **Logging**
  - Provides logging for key operations such as UTXO creation, transaction processing, and errors.

## How to Use
1. Clone or download the repository.
2. Install the required dependencies using `pip install cryptography`.
3. Run the `main.py` script to simulate a blockchain environment with transactions between Alice, Bob, and Charlie.

## Example Workflow
1. **Alice** generates a UTXO with 100 coins and sends 30 coins to **Bob**.
2. **Bob** then sends 20 coins to **Charlie**.
3. The system ensures that Alice and Bob have sufficient funds and creates new UTXOs accordingly.

## Code Explanation

### `utxo.py`
- **Blockchain Class:**
  - Manages the UTXO set and ledger of transactions.
  - Supports methods to generate private/public key pairs (`generate_keys`), create new UTXOs (`create_utxo`), sign transactions (`sign_transaction`), and verify transactions (`verify_transaction`).
  - The `process_transaction` method handles the logic for transferring funds, verifying the transaction, and updating the UTXO set.

### `main.py`
- **Main Functionality:**
  - Demonstrates how the Blockchain class can be used to simulate transactions between Alice, Bob, and Charlie.
  - It first creates an initial UTXO for Alice, then processes transactions between users, printing the UTXO set at each stage.

## Sample Output:
```yaml
Created UTXO: 98e9e6f9e2d47dffed9b77c13ec4fcb48fd8f4ea8f1d40e4b8c5a8273952ba76 for Alice with amount 100
Current UTXO Set:
UTXO: 98e9e6f9e2d47dffed9b77c13ec4fcb48fd8f4ea8f1d40e4b8c5a8273952ba76, Amount: 100, Recipient: Alice

Transaction processed: Alice sent 30 to Bob
Current UTXO Set:
UTXO: 98e9e6f9e2d47dffed9b77c13ec4fcb48fd8f4ea8f1d40e4b8c5a8273952ba76, Amount: 70, Recipient: Alice
UTXO: 1284c11c42380f29f9cde543a2e31f2e3a98842a4a2633d66b4b70f94d6b0f52, Amount: 30, Recipient: Bob

Transaction processed: Bob sent 20 to Charlie
Current UTXO Set:
UTXO: 98e9e6f9e2d47dffed9b77c13ec4fcb48fd8f4ea8f1d40e4b8c5a8273952ba76, Amount: 70, Recipient: Alice
UTXO: 1284c11c42380f29f9cde543a2e31f2e3a98842a4a2633d66b4b70f94d6b0f52, Amount: 10, Recipient: Bob
UTXO: b3f3ac98fca1a50dbf9cf1e0cf30be51b25f62a7b923d1be328c82a6c498e7a9, Amount: 20, Recipient: Charlie
```

## Running the Project
```bash
Clone the repository (if you haven’t already):

git clone https://github.com/your-username/utxo-blockchain.git
cd utxo-blockchain
Install dependencies:

pip install -r requirements.txt
Run the script:

python main.py
```
## Future Enhancements
Implement additional blockchain features like block mining, proof-of-work, and block validation.
Integrate a peer-to-peer network for decentralized transaction processing.
Implement a more complex UTXO management system (e.g., handling change and more granular transaction outputs).
