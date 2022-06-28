from flask import Flask, request, jsonify
from parser import main

app = Flask(__name__)


@app.post('/')
def index():

    return jsonify(main(request.json))

if __name__ == '__main__':
    app.run(debug=True)
