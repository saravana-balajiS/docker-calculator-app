from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/add')
def add():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = num1 + num2
    r.set('last_result', result)
    return jsonify({'operation': 'add', 'result': result})

@app.route('/subtract')
def subtract():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = num1 - num2
    r.set('last_result', result)
    return jsonify({'operation': 'subtract', 'result': result})

@app.route('/multiply')
def multiply():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = num1 * num2
    r.set('last_result', result)
    return jsonify({'operation': 'multiply', 'result': result})

@app.route('/divide')
def divide():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    if num2 == 0:
        return jsonify({'error': 'Cannot divide by zero'}), 400
    result = num1 / num2
    r.set('last_result', result)
    return jsonify({'operation': 'divide', 'result': result})

@app.route('/last')
def last():
    result = r.get('last_result') or "No result yet"
    return jsonify({'last_result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
