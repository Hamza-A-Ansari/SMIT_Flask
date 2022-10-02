from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return __name__

app.run(debug=True)
