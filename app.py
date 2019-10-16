from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/customers')
def get_customers():
    return '<h1>Customers</h1>'


@app.route('/customer/<name>')
def get_customer(name):
    return 'Hello, {}'.format(name)


# launch Flask web server
if __name__ == '__main__':
    app.run()
