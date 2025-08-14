from flask import Flask

app = Flask(__name__)

# We'll intentionally change this line differently on two branches later
GREETING = "Hello from main branch!"

@app.route("/")
def hello():
    # Just a simple log so you can see requests in the console
    print("Request received at /")
    return GREETING

if __name__ == "__main__":
    app.run(debug=True)
