from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Docker Compose CI/CD Project!"

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "Docker Compose CI/CD"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    