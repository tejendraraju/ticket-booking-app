from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    ticket = request.form['ticket']
    quantity = request.form['quantity']

    return render_template('success.html', name=name, ticket=ticket, quantity=quantity)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)