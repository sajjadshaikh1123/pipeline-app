from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from CI/CD pipeline - build {os.environ.get('BUILD_NUM','local')}\n"

@app.route("/healthz")
def health():
    return "ok\n"

app.run(host="0.0.0.0", port=5000)
