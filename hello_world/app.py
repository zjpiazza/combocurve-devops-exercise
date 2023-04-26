from flask import Flask

app = Flask(__name__)

COUNT = 0

@app.route("/")
def hello():
    COUNT += 1
    return f"Hello World!!! I have been called {COUNT} times."
