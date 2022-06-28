from flask import Flask, request, jsonify
from parser import main
import os

app = Flask(__name__)


@app.post('/')
def index():
    return jsonify(main(request.json))


PORT = 5000
if __name__ == '__main__':
    print(f'Server started in port {PORT}')
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', PORT)))
