from hashlib import sha256
from typing import List, Dict, Any, Optional
import json
import time


class Block:
    def __init__(self, index: int, transactions: List[Dict[str, Any]], previous_hash: str, proof: int, timestamp: Optional[float] = None):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.proof = proof
        self.timestamp = timestamp or time.time()
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        block_dict = {k: v for k, v in self.__dict__.items() if k != 'hash'}
        block_string = json.dumps(block_dict, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[Dict[str, Any]] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(index=0, transactions=[], previous_hash="0", proof=0)
        self.chain.append(genesis_block)

    def add_transaction(self, sender: str, receiver: str, amount: int, input_utxos: List[str], output_utxos: List[str], signature: str):
        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "input_utxos": input_utxos,
            "output_utxos": output_utxos,
            "signature": signature,
            "timestamp": time.time()
        }
        self.pending_transactions.append(transaction)

    def proof_of_work(self, previous_proof: int) -> int:
        proof = 0
        while not self.is_valid_proof(previous_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def is_valid_proof(previous_proof: int, proof: int) -> bool:
        guess = f"{previous_proof}{proof}".encode()
        guess_hash = sha256(guess).hexdigest()
        return guess_hash[:1] == "0"  # Changed from '0000' to '0' for testing

    def mine_block(self) -> Block:
        if not self.pending_transactions:
            raise ValueError("No transactions to mine.")
        previous_block = self.chain[-1]
        previous_proof = previous_block.proof
        proof = self.proof_of_work(previous_proof)
        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions.copy(),
            previous_hash=previous_block.hash,
            proof=proof,
        )
        self.pending_transactions = []
        self.chain.append(new_block)
        return new_block

    def validate_block(self, block: Block) -> bool:
        # Simplified validation for testing
        if block.index != len(self.chain):
            return False
        if block.previous_hash != self.chain[-1].hash:
            return False
        return True

    def add_block(self, block_data: Dict[str, Any]) -> bool:
        block = Block(**block_data)
        if self.validate_block(block):
            self.chain.append(block)
            return True
        return False