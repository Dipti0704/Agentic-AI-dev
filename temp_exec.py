from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
todos = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Walk the dog", "done": True}
]

@app.route('/api/todos', methods=['GET'])
def get_all_todos():
    return jsonify(todos)

@app.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify(todo)

@app.route('/api/todos', methods=['POST'])
def create_todo():
    new_todo = {
        'id': len(todos) + 1,
        'title': request.json['title'],
        'done': False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

if __name__ == '__main__':
    app.run(debug=True)