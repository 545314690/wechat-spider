from flask import Flask
from flask_script import Manager

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


mamager = Manager(app)


if __name__ == '__main__':
    # app.run(debug=True)
    mamager.run()