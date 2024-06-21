from flask import Flask, jsonify
import time
import random
import cProfile
import pstats
import io

app = Flask(__name__)

# Simulate a large dataset
large_dataset = [{"id": i, "value": random.randint(1, 1000)} for i in range(1000000)]

# Pre-sample data to avoid doing it on every request
pre_sampled_data = [random.sample(large_dataset, 10) for _ in range(100)]

@app.route('/data', methods=['GET'])
def get_data():
    start_time = time.perf_counter()  # More precise timing
    pr = cProfile.Profile()
    pr.enable()

    # Retrieve a pre-sampled data set to minimize processing time
    sample_data = random.choice(pre_sampled_data)
    data = {
        "message": "Hello, this is your data!",
        "timestamp": time.time(),
        "sample_data": sample_data
    }

    pr.disable()
    s = io.StringIO()
    sortby = pstats.SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())

    response_time = time.perf_counter() - start_time
    if response_time > 1:
        return jsonify({"error": "Response took too long!"}), 500
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
