import os
import uuid

import stripe
from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

TODOS = [
    {
        'id': uuid.uuid4().hex,
        'todo': 'On the Road2',
        'assignee': 'Jack Kerouac2',
        'done': True
    },
    {
        'id': uuid.uuid4().hex,
        'todo': 'On the Road3',
        'assignee': 'Jack Kerouac3',
        'done': False
    },
    {
        'id': uuid.uuid4().hex,
        'todo': 'On the Road4',
        'assignee': 'Jack Kerouac4',
        'done': True
    }
]


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/todos', methods=['GET', 'POST'])
def all_todos():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        TODOS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read'),
            'price': post_data.get('price')
        })
        response_object['message'] = 'todos added!'
    else:
        response_object['todos'] = TODOS
    return jsonify(response_object)


@app.route('/todos/<todos_id>', methods=['GET', 'PUT', 'DELETE'])
def single_todos(todos_id):
    response_object = {'status': 'success'}
    if request.method == 'GET':
        # TODO: refactor to a lambda and filter
        return_todos = ''
        for todos in TODOS:
            if todos['id'] == todos_id:
                return_todos = todos
        response_object['todos'] = return_todos
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_todos(todos_id)
        TODOS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read'),
            'price': post_data.get('price')
        })
        response_object['message'] = 'todos updated!'
    if request.method == 'DELETE':
        remove_todos(todos_id)
        response_object['message'] = 'todos removed!'
    return jsonify(response_object)


@app.route('/charge', methods=['POST'])
def create_charge():
    post_data = request.get_json()
    amount = round(float(post_data.get('todos')['price']) * 100)
    stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
    charge = stripe.Charge.create(
        amount=amount,
        currency='usd',
        card=post_data.get('token'),
        description=post_data.get('todos')['title']
    )
    response_object = {
        'status': 'success',
        'charge': charge
    }
    return jsonify(response_object), 200


@app.route('/charge/<charge_id>')
def get_charge(charge_id):
    stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
    response_object = {
        'status': 'success',
        'charge': stripe.Charge.retrieve(charge_id)
    }
    return jsonify(response_object), 200


def remove_todos(todos_id):
    for todos in TODOS:
        if todos['id'] == todos_id:
            TODOS.remove(todos)
            return True
    return False


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)
