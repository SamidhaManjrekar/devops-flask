from flask import Flask

app = Flask(__name__)

GREETING = "Hello from user-auth!"

@app.route("/")
def hello():
    print("Request received at /")
    return GREETING

if __name__ == "__main__":
    app.run(debug=True)
