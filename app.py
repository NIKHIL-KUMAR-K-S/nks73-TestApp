from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to devops-starter!</h1>"

@app.route('/health')
def health():
    return jsonify(status="ok")

@app.route('/ready')
def ready():
    return jsonify(status="ready")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
