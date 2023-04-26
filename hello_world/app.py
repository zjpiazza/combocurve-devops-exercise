from flask import Flask

app = Flask(__name__)

COUNT = 0

@app.route("/")
def hello():
    global COUNT
    COUNT += 1
    
    return {
        "message": "Hello World!!!",
        "invocation_count": COUNT
    }