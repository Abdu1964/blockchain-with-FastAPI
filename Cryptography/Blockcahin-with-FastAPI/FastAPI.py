from fastapi import FastAPI, HTTPException
from blockchain import Blockchain, Block
from typing import Dict, Any

app = FastAPI()
blockchain = Blockchain()


@app.post("/mine_block")
def mine_block() -> Dict[str, Any]:
    try:
        block = blockchain.mine_block()
        return {"message": "Block mined successfully!", "block": block.__dict__}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/new_transaction")
def new_transaction(transaction: Dict[str, Any]) -> Dict[str, str]:
    required_fields = {"sender", "receiver", "amount", "input_utxos", "output_utxos", "signature"}
    if not required_fields.issubset(transaction.keys()):
        raise HTTPException(status_code=400, detail="Missing transaction fields.")
    blockchain.add_transaction(**transaction)
    return {"message": "Transaction added to pending list."}


@app.post("/add_block")
def add_block(block_data: Dict[str, Any]) -> Dict[str, str]:
    if blockchain.add_block(block_data):
        return {"message": "Block added to the chain."}
    raise HTTPException(status_code=400, detail="Invalid block.")


@app.get("/chain")
def get_chain() -> Dict[str, Any]:
    chain_data = [block.__dict__ for block in blockchain.chain]
    return {"length": len(chain_data), "chain": chain_data}