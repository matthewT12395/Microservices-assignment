# user_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user "database"
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    user_id = max(users.keys()) + 1 if users else 1  # handle empty dict
    users[user_id] = new_user
    return jsonify({"user_id": user_id}), 201


if __name__ == '__main__':
    app.run(port=5001, debug=True)
