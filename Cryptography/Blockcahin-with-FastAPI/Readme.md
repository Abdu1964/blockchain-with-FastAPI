Blockchain FastAPI Implementation
This project implements a simple blockchain with FastAPI endpoints to mine new blocks, accept transactions, add blocks to the chain, and fetch the current blockchain. It demonstrates basic blockchain concepts and validation using Python and FastAPI.

Objective
The goal of this project is to implement FastAPI endpoints for the following blockchain functionalities:

Mining a new block.
Accepting new transactions.
Adding received blocks to the chain.
Additionally, a /chain endpoint is provided to return the current blockchain.

Requirements
Endpoints:
/mine_block: Trigger mining of a new block and add it to the chain.

Method: POST
Response: Success or error message with the mined block data.
/new_transaction: Accept transaction data (sender, receiver, amount, input utxos, output utxos, signature) and add it to a list of pending transactions.

Method: POST
Body:
json
Copy code
{
  "sender": "sender_address",
  "receiver": "receiver_address",
  "amount": 10,
  "input_utxos": ["utxo1", "utxo2"],
  "output_utxos": ["utxo3", "utxo4"],
  "signature": "transaction_signature"
}
Response: Success message.
/add_block: Accept a block (e.g., from another node) and validate it before appending to the chain.

Method: POST
Body:
json
Copy code
{
  "index": 1,
  "transactions": [{"sender": "sender_address", "receiver": "receiver_address", "amount": 10}],
  "previous_hash": "previous_hash_value",
  "proof": 123456,
  "timestamp": 1638246823
}
Response: Success or error message.
/chain: Returns the current blockchain.

Method: GET
Response: List of all blocks in the blockchain.
Blockchain Functions:
Mining: The blockchain mines a new block by solving a proof-of-work problem, validating transactions, and appending the block to the chain.
Transactions: Transactions are added to a pending list and mined into a block when a new block is created.
Block Validation: Blocks are validated before being added to the chain to ensure they are properly linked and meet consensus rules.
How to Run
Requirements:
Python 3.x
Install dependencies:
bash
Copy code
pip install fastapi uvicorn
Running the FastAPI Application:
Save the provided blockchain.py and fastapi.py files to your project directory.
Run the FastAPI app with:
bash
Copy code
uvicorn fastapi:app --reload
Open a browser and go to http://127.0.0.1:8000/docs to interact with the API using the automatically generated Swagger UI.
Example of Usage:
Mine a block:

POST to /mine_block.
The server will mine a new block and add it to the chain.
Add a new transaction:

POST to /new_transaction with transaction data.
Add a received block:

POST to /add_block with block data.
Get the blockchain:

GET to /chain to retrieve the current blockchain.
Code Explanation
blockchain.py:
This file contains the logic for the blockchain, including block creation, mining, transaction handling, and block validation. It defines two classes:

Block: Represents a single block in the blockchain.
Blockchain: Manages the chain, mining process, transactions, and block validation.
fastapi.py:
This file contains the FastAPI endpoints for interacting with the blockchain. It defines routes for:

Mining blocks (/mine_block).
Adding transactions (/new_transaction).
Adding blocks (/add_block).
Retrieving the chain (/chain).
Features and Enhancements:
Basic Proof-of-Work: Implements a simple proof-of-work algorithm where the hash of the proof must start with a "0" (to simulate difficulty).
Transaction Handling: Pending transactions are collected and mined into blocks.
Block Validation: Before adding any new block to the chain, the block is validated against the previous block's hash and index.
Possible Enhancements:
Consensus Mechanism: Improve the consensus by implementing a more sophisticated algorithm for validating blocks across multiple nodes.
Blockchain UI: Create a user interface to display the blockchain and transaction history.
Transaction Pool: Manage pending transactions with more complex structures.