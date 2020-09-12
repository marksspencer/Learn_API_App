## Here is where the app will be.

## Let's get the basic setup done:
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    