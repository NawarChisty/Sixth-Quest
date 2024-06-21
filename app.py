from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    start_time = time.time()
    data = {
        "message": "Hello, this is your data!",
        "timestamp": time.time()
    }
    response_time = time.time() - start_time
    if response_time > 1:
        return jsonify({"error": "Response took too long!"}), 500
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
