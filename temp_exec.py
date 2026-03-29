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

# API route to create a new todo
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    todo = {'id': len(open('todo.txt').readlines()) + 1, 'title': data['title'], 'done': False}
    with open('todo.txt', 'a') as f:
        f.write(f"{todo['id']}: {todo['title']} - {str(todo['done'])}\n")
    return jsonify({'message': 'Todo created successfully'})

if __name__ == '__main__':
    app.run(debug=True)