from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample user data
users = {
    "user1": {"balance": 1000, "transactions": []},
    "user2": {"balance": 500, "transactions": []}
}

@app.route("/")
def home():
    return "Welcome to Online Banking Demo!"

@app.route("/balance/<username>", methods=["GET"])
def get_balance(username):
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"balance": user["balance"]})

@app.route("/transfer", methods=["POST"])
def transfer():
    data = request.json
    sender = users.get(data.get("from"))
    receiver = users.get(data.get("to"))
    amount = data.get("amount", 0)

    if not sender or not receiver:
        return jsonify({"error": "Invalid users"}), 400
    if sender["balance"] < amount:
        return jsonify({"error": "Insufficient balance"}), 400

    sender["balance"] -= amount
    receiver["balance"] += amount

    sender["transactions"].append(f"Sent {amount} to {data.get('to')}")
    receiver["transactions"].append(f"Received {amount} from {data.get('from')}")

    return jsonify({"message": "Transfer successful"})

@app.route("/transactions/<username>", methods=["GET"])
def transactions(username):
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"transactions": user["transactions"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
