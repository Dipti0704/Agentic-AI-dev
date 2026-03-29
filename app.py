from flask import Flask, jsonify, request

app = Flask(__name__)

# API route to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = [
        {'id': 1, 'title': 'Task 1', 'description': 'This is task 1'},
        {'id': 2, 'title': 'Task 2', 'description': 'This is task 2'}
    ]
    return jsonify({'tasks': tasks})

# API route to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = {'id': len(tasks) + 1, 'title': data['title'], 'description': data['description']}
    tasks.append(task)
    return jsonify({'task': task})

if __name__ == '__main__':
    app.run(debug=True)