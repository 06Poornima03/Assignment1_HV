from flask import Flask
app = Flask(__name__)

@app.route("/")
def get_Welcome():
    return{"msg":"Welcome to the app"}

@app.route("/health")
def get_health():
    return{"msg":"App is running"}
