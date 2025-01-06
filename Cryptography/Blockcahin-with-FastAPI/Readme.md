# Simple Blockchain with FastAPI

This project implements a basic blockchain using Python and FastAPI. The blockchain includes functionality for:
- Mining blocks
- Accepting transactions
- Adding blocks to the blockchain
- Validating the blockchain
- Providing the current chain

## Features
- **Mining a new block**: Uses proof of work to mine new blocks and add them to the blockchain.
- **Adding a transaction**: Accepts transaction data and adds it to the list of pending transactions.
- **Adding a block**: Accepts a block from another node, validates it, and adds it to the blockchain.
- **Viewing the blockchain**: Provides the full blockchain with all its blocks.
- **Validating the blockchain**: A check to validate if the entire blockchain is consistent.

## Requirements
- Python 3.7 or higher
- FastAPI
- Uvicorn
- SHA256 library (Standard Python library)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/blockchain-fastapi.git
    cd blockchain-fastapi
    ```

2. Install the dependencies:
    ```bash
    pip install fastapi uvicorn
    ```

3. Run the FastAPI server:
    ```bash
    uvicorn fastapi:app --reload
    ```

4. Open your browser and navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to interact with the API.

## Endpoints

### `POST /mine_block`
- Mines a new block and adds it to the blockchain.
- Returns: The mined block's data.

### `POST /new_transaction`
- Adds a new transaction to the list of pending transactions.
- Required parameters: `sender`, `receiver`, `amount`, `input_utxos`, `output_utxos`, `signature`.

### `POST /add_block`
- Accepts a block from another node and validates it before adding it to the blockchain.
- Required parameters: Block data.

### `GET /chain`
- Returns the current blockchain in JSON format.

### `GET /validate_chain`
- Validates the entire blockchain to ensure it is valid.

## Blockchain Design
- **Genesis Block**: The first block in the chain, created with no transactions.
- **Proof of Work**: A mining algorithm that involves finding a valid proof for the next block.
- **Transaction**: A record containing the sender, receiver, amount, input UTXOs, output UTXOs, and signature.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
