from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    # return 'Hello World!'
    return render_template('index.html')


@app.route('/customers')
def get_customers():
    return '<h1>Customers</h1>'


@app.route('/customer/<name>')
def get_customer(name):
    return 'Hello, {}'.format(name)


@app.route('/user/<name>')
def get_user(name):
    return render_template('user.html',name=name)


# launch Flask web server
if __name__ == '__main__':
    app.run()
