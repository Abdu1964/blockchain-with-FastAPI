from utxo import Blockchain

def main():
    # Initialize the blockchain
    blockchain = Blockchain()

    # Generate keys for Alice and Bob
    alice_private_key, alice_public_key = blockchain.generate_keys()
    bob_private_key, bob_public_key = blockchain.generate_keys()

    # Initial UTXO for Alice
    blockchain.create_utxo("Alice", 100)

    # Print initial UTXO set
    blockchain.print_utxo_set()

    # Alice sends 30 coins to Bob
    try:
        blockchain.process_transaction(
            sender="Alice",
            recipient="Bob",
            amount=30,
            private_key=alice_private_key,
            public_key=alice_public_key,
        )
    except ValueError as e:
        print(f"Transaction Error: {e}")

    # Print UTXO set after Alice's transaction
    blockchain.print_utxo_set()

    # Bob sends 20 coins to Charlie
    try:
        blockchain.process_transaction(
            sender="Bob",
            recipient="Charlie",
            amount=20,
            private_key=bob_private_key,
            public_key=bob_public_key,
        )
    except ValueError as e:
        print(f"Transaction Error: {e}")

    # Print UTXO set after Bob's transaction
    blockchain.print_utxo_set()


if __name__ == "__main__":
    main()
