from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/<string:Text>')
def print_string(Text):
    List=[]
    List.append(Text)
    return f'''<ul>
        <li>{Text}</li>
        </ul>'''
        
@app.route('/count/<int:Num>')
def count(Num):
    i=0
    for i in range(Num+1):
        output="\n".join(str(i))
    return f'<pre>{output}</pre>'

@app.route('/math/<int:num1>/<operation>/<int:num2>', methods=['GET'])
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return ("Cannot divide by zero.")
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return ("Invalid operation.")

    return f"The result of {num1} {operation} {num2} is: {result}"




if __name__ == '__main__':
    app.run(port=5555, debug=True)
