import hashlib
import random
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey, EllipticCurvePublicKey
from cryptography.hazmat.primitives import hashes
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Blockchain:
    def __init__(self):
        self.utxo_set = {}
        self.ledger = []

    def generate_keys(self) -> tuple[EllipticCurvePrivateKey, EllipticCurvePublicKey]:
        """Generate a private and public key pair."""
        private_key = ec.generate_private_key(ec.SECP256R1())
        public_key = private_key.public_key()
        return private_key, public_key

    def create_utxo(self, recipient: str, amount: int) -> str:
        """Create a UTXO and add it to the UTXO set."""
        utxo_id = hashlib.sha256(f"{recipient}{amount}{random.random()}".encode()).hexdigest()
        self.utxo_set[utxo_id] = {"amount": amount, "recipient": recipient}
        logging.info(f"Created UTXO: {utxo_id} for {recipient} with amount {amount}")
        return utxo_id

    def sign_transaction(self, private_key: EllipticCurvePrivateKey, sender: str, recipient: str, amount: int) -> bytes:
        """Sign a transaction with the sender's private key."""
        message = f"{sender}|{recipient}|{amount}"
        return private_key.sign(message.encode("utf-8"), ec.ECDSA(hashes.SHA256()))

    def verify_transaction(
        self, public_key: EllipticCurvePublicKey, sender: str, recipient: str, amount: int, signature: bytes
    ) -> bool:
        """Verify a transaction signature."""
        message = f"{sender}|{recipient}|{amount}"
        try:
            public_key.verify(signature, message.encode("utf-8"), ec.ECDSA(hashes.SHA256()))
            return True
        except Exception:
            return False

    def process_transaction(
        self,
        sender: str,
        recipient: str,
        amount: int,
        private_key: EllipticCurvePrivateKey,
        public_key: EllipticCurvePublicKey,
    ):
        """Process a transaction by transferring funds and updating the UTXO set."""
        sender_utxos = {utxo_id: utxo for utxo_id, utxo in self.utxo_set.items() if utxo["recipient"] == sender}
        sender_balance = sum(utxo["amount"] for utxo in sender_utxos.values())

        if sender_balance < amount:
            raise ValueError(f"{sender} does not have enough funds for this transaction!")

        signature = self.sign_transaction(private_key, sender, recipient, amount)
        if not self.verify_transaction(public_key, sender, recipient, amount, signature):
            raise ValueError("Transaction verification failed!")

        consumed_amount = 0
        for utxo_id, utxo in list(sender_utxos.items()):
            del self.utxo_set[utxo_id]
            consumed_amount += utxo["amount"]
            if consumed_amount >= amount:
                break

        self.create_utxo(recipient, amount)
        if consumed_amount > amount:
            self.create_utxo(sender, consumed_amount - amount)

        logging.info(f"Transaction processed: {sender} sent {amount} to {recipient}")

    def print_utxo_set(self):
        """Print the current UTXO set."""
        logging.info("Current UTXO Set:")
        for utxo_id, utxo in self.utxo_set.items():
            print(f"UTXO: {utxo_id}, Amount: {utxo['amount']}, Recipient: {utxo['recipient']}")
