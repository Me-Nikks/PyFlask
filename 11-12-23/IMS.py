from flask import Flask, request, jsonify

app = Flask(__name__)  # app const

data = [
    {'id': 1, 'name': 'Bibin', 'phone': '6451515'},
    {'id': 2, 'name': 'Nikhil', 'phone': '6451515'},
    {'id': 3, 'name': 'Varsha', 'phone': '6451515'},
    {'id': 4, 'name': 'Sridhar', 'phone': '6451515'},
    {'id': 5, 'name': 'Srujan', 'phone': '6451515'},
    {'id': 6, 'name': 'Ziya', 'phone': '6451515'},
]


# RESTFUL APIs
@app.route('/all_users', methods=['GET'])
def get_users():
    return jsonify({'users': data})


def find_user(user_id):
    return next((user for user in data if user['id'] == user_id), None)


@app.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = find_user(user_id)
    return jsonify({'user_details': user})


@app.route('/add_user', methods=['POST'])
def add_user():
    user = request.get_json()
    new_user = {'id': len(data) + 1, 'name': user['name'], 'phone': user['phone']}
    data.append(new_user)
    return jsonify({'message': 'User created'}), 201


@app.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = find_user(user_id)
    if user:
        user_data = request.get_json()
        user['name'] = data['name']
        user['phone'] = data['phone']
        return jsonify({'message': 'User updated', 'updated_user_details': user_data})
    else:
        return jsonify({'message': 'User not found'}), 404


@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global data
    data = [user for user in data if data["id"] != user_id]
    return jsonify({'message': 'user deleted'})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="81", debug=True)
