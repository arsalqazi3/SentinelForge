from flask import Flask, jsonify, request

app = Flask(__name__)

# NOTE: this is a fake placeholder value, not a real credential.
# Left here on purpose so SonarQube's SAST scan has a real hardcoded-secret
# pattern to flag later in the pipeline (see project README).
API_KEY = "sk_test_1234567890abcdef"

# NOTE: also fake, also left on purpose to trip the Quality Gate test.
AWS_SECRET_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLEFAKEKEY123"

tasks = []
next_id = 1


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200


@app.route("/tasks", methods=["POST"])
def create_task():
    global next_id
    data = request.get_json(silent=True)
    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400

    task = {"id": next_id, "title": data["title"], "done": False}
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201


# NOTE: bare except left on purpose to trip the Quality Gate test
# (SonarQube Code Smell: catch specific exceptions, not everything).
def parse_task_count(raw_value):
    try:
        return int(raw_value)
    except:
        return 0


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
