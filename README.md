Blockchain FastAPI & UTXO Blockchain Implementation
Overview
This project demonstrates two blockchain implementations:

Blockchain FastAPI Implementation - A simple blockchain with FastAPI endpoints for mining blocks, accepting transactions, adding blocks, and fetching the blockchain.
UTXO Blockchain Implementation - A blockchain using the Unspent Transaction Output (UTXO) model to handle transactions, including UTXO generation, signing, verification, and processing.
Blockchain FastAPI Implementation
Objective
The goal is to implement FastAPI endpoints to manage blockchain functionalities:

Mining a new block.
Accepting new transactions.
Adding received blocks to the chain.
Fetching the current blockchain.
Requirements
Python 3.x
FastAPI and Uvicorn for serving the application.
Endpoints:
/mine_block: Triggers mining of a new block and adds it to the chain.

Method: POST
Response: Success or error message with mined block data.
/new_transaction: Accepts transaction data (sender, receiver, amount, input UTXOs, output UTXOs, signature) and adds it to a list of pending transactions.

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
/add_block: Accepts a block and validates it before appending it to the chain.

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
Mining: Mines new blocks via a proof-of-work algorithm.
Transactions: Adds pending transactions to a mined block.
Block Validation: Ensures blocks are valid before adding them to the chain.
How to Run:
Install dependencies:

bash
Copy code
pip install fastapi uvicorn
Run the FastAPI app:

bash
Copy code
uvicorn fastapi:app --reload
Open the browser and go to http://127.0.0.1:8000/docs to interact with the API using Swagger UI.

Example Usage:
Mine a Block: POST to /mine_block.
Add a New Transaction: POST to /new_transaction with transaction data.
Add a Block: POST to /add_block with block data.
Get the Blockchain: GET to /chain to retrieve the current blockchain.
Code Explanation:
blockchain.py: Contains the blockchain logic (block creation, mining, transactions).
fastapi.py: Defines FastAPI endpoints for interacting with the blockchain.
Features and Enhancements:
Proof-of-Work: Simple proof-of-work where the hash of the proof must start with a "0".
Transaction Handling: Transactions are added to the chain once mined.
Block Validation: Ensures blocks are properly linked.
Future Enhancements:
Consensus Mechanism: Implement a more advanced algorithm for block validation across multiple nodes.
Blockchain UI: Create an interface to visualize the blockchain.
Transaction Pool: Manage pending transactions with a more complex system.
UTXO Blockchain Implementation
Overview
This part demonstrates a blockchain using the UTXO (Unspent Transaction Output) model to manage transactions. It includes UTXO creation, signing, verifying, and processing transactions between users.

Project Structure:
bash
Copy code
/your-project
├── utxo.py              # Blockchain implementation (class with UTXO management and transaction processing)
└── main.py              # Script to run the blockchain example with Alice, Bob, and Charlie
Requirements:
Python 3.8+
cryptography package: Install via pip install cryptography.
Features:
UTXO Management: Generates and tracks UTXOs in a dictionary (utxo_set).
Transaction Signing and Verification: Uses elliptic curve cryptography (ECC) for signing and verifying transactions.
Blockchain Transaction Processing: Handles funds transfer between users, updates the UTXO set, and manages balances.
Logging: Logs key operations like UTXO creation and transaction processing.
How to Use:
Clone or download the repository.
Install required dependencies:
bash
Copy code
pip install cryptography
Run the main.py script to simulate transactions between Alice, Bob, and Charlie.
Example Workflow:
Alice generates a UTXO with 100 coins and sends 30 coins to Bob.
Bob sends 20 coins to Charlie.
The UTXO set is updated and printed after each transaction.
Example Output:

vbnet
Copy code
Created UTXO for Alice with amount 100
Current UTXO Set: Alice's UTXO of 100
Transaction processed: Alice sent 30 to Bob
Current UTXO Set: Alice's UTXO of 70, Bob's UTXO of 30
Transaction processed: Bob sent 20 to Charlie
Current UTXO Set: Alice's UTXO of 70, Bob's UTXO of 10, Charlie's UTXO of 20
Code Explanation:
utxo.py: Implements blockchain logic with UTXO management, including generating keys, creating and verifying UTXOs, and processing transactions.
main.py: Demonstrates transaction processing between Alice, Bob, and Charlie, printing the UTXO set after each transaction.
Running the Project:
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/utxo-blockchain.git
cd utxo-blockchain
Install dependencies:
bash
Copy code
pip install cryptography
Run the script:
bash
Copy code
python main.py
Future Enhancements:
Block Mining and Proof-of-Work: Implement mining and validation features.
Peer-to-Peer Network: Implement a decentralized transaction processing system.
Advanced UTXO Management: Handle change and granular transaction outputs.
