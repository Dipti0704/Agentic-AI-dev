from flask import Flask, jsonify, request

app = Flask(__name__)

# API route to get all todos
@app.route('/todos', methods=['GET'])
def get_all_todos():
    todos = [
        {'id': 1, 'title': 'Buy milk', 'done': False},
        {'id': 2, 'title': 'Walk the dog', 'done': True}
    ]
    return jsonify({'todos': todos})

# API route to add a new todo
@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    todo = {'id': len(todos) + 1, 'title': data['title'], 'done': False}
    todos.append(todo)
    return jsonify({'todo': todo})

if __name__ == '__main__':
    app.run(debug=True)