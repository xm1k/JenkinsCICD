from flask import Flask, request, jsonify
from alg import process_input

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    payload = request.get_json(force=True)
    inp = payload.get('input', '')
    out = process_input(inp)
    return jsonify({'output': out})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
