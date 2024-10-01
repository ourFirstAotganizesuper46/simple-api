
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Index!"



@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    return "Hello, " + str(name)

@app.route('/getcode', methods=['GET'])
def getcode():
    return jsonify({ 'code' : 200, 'message' : 'whatever 333' })

@app.route('/is_prime/<int:number>', methods=['GET'])
def is_prime(number):
    if number <= 1:
        return {'result': False}
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return {'result': False}
    return {'result': True}

@app.route('/is_fibonacci/<int:number>', methods=['GET'])
def is_fibonacci(number):
    x, y = 0, 1
    while y < number:
        x, y = y, x + y
    result = (y == number)
    return {'result': result}

@app.route('/plus/<num1>/<num2>', methods=['GET'])
def plus(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        results = { 'result' : num1 + num2 }
    except:
        results = { 'error_msg' : 'inputs must be numbers' }

    return results


@app.route('/calculate/<num1>/<num2>', methods=['GET'])
def calculate(num1, num2):
    try:
        num1 = float(num1)
        num2 = int(num2)

        results = {
                'plus' : num1 + num2,
                'minus' : num1 - num2,
                'multiply': num1 * num2,
                'divide' : num1/num2
            }
    except:
        results = { 'error_msg' : 'inputs must be numbers' }

    return jsonify(results)


if __name__ == '__main__':
    app.run()
