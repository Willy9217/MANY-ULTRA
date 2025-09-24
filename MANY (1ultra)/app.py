from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "MANY Ultra está vivo."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(__import__('os').environ.get('PORT', 5000)))
