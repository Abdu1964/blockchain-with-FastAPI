import requests

BASE_URL = "http://127.0.0.1:8000"  # Update the URL if your server is hosted elsewhere

# Test 1: Root endpoint
def test_root():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Blockchain API!"}

# Test 2: Mine Block endpoint
def test_mine_block():
    response = requests.post(f"{BASE_URL}/mine_block")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "block" in data
    assert data["message"] == "Block mined successfully!"

# Test 3: Add Transaction
def test_new_transaction():
    transaction = {
        "sender": "Alice",
        "receiver": "Bob",
        "amount": 50,
        "input_utxos": ["tx1", "tx2"],
        "output_utxos": ["tx3", "tx4"],
        "signature": "some_signature"
    }
    response = requests.post(f"{BASE_URL}/new_transaction", json=transaction)
    assert response.status_code == 200
    assert response.json() == {"message": "Transaction added to pending list."}

# Test 4: Add Block endpoint
def test_add_block():
    block_data = {
        "index": 1,
        "transactions": [{"sender": "Alice", "receiver": "Bob", "amount": 50, "input_utxos": ["tx1"], "output_utxos": ["tx3"], "signature": "some_signature"}],
        "previous_hash": "5b987a3af6b054bc005166bec3b83c5fc10626596a76e103ed282e0e92d2a1b1",
        "proof": 69732
    }
    response = requests.post(f"{BASE_URL}/add_block", json=block_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Block added to the chain."}

# Test 5: Get Blockchain
def test_get_chain():
    response = requests.get(f"{BASE_URL}/chain")
    assert response.status_code == 200
    assert "chain" in response.json()

# Test 6: Get Last Block
def test_get_last_block():
    response = requests.get(f"{BASE_URL}/get_last_block")
    assert response.status_code == 200
    assert "previous_hash" in response.json()
    assert "proof" in response.json()
    assert "hash" in response.json()

if __name__ == "__main__":
    test_root()
    test_mine_block()
    test_new_transaction()
    test_add_block()
    test_get_chain()
    test_get_last_block()
    print("All tests passed!")
