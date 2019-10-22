from flask import Flask, render_template

from flask import jsonify
from templates.infrastructure.view_modifiers  import response
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


def get_latest_packages():
    return [
        {'name': 'flask', 'version': '1.2.3'},
        {'name': 'sqlalchemy', 'version': '2.2.0'},
        {'name': 'passlib', 'version': '3.0.0'},
    ]


@app.route('/')
@response(template_file='home/index.html')
def index():
    test_packages = get_latest_packages()
    return {'packages': test_packages}
    # return flask.render_template('home/index.html', packages=test_packages)


@app.route('/about')
@response(template_file='home/about.html')
def about():
    return {}


@app.route('/map')
@response(template_file='GIS/map.html')
def map():
    return {}


@app.route('/api/documents', methods=['GET'])
def get_all():
    return jsonify({'tasks': tasks})


# @app.route('/')
# def hello_world():
#     # return 'Hello World!'
#     return render_template('index.html')
#
#
# @app.route('/customers')
# def get_customers():
#     return '<h1>Customers</h1>'
#
#
# @app.route('/customer/<name>')
# def get_customer(name):
#     return 'Hello, {}'.format(name)
#
#
# @app.route('/user/<name>')
# def get_user(name):
#     return render_template('user.html',name=name)


# launch Flask web server
if __name__ == '__main__':
    app.run()
