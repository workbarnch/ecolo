from main import app
import os

PORT = 5000
if __name__ == '__main__':
    print(f'Server started in port {PORT}')
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', PORT)))
