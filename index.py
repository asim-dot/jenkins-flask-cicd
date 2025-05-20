from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Vercel!"

@app.route('/<path:path>')
def catch_all(path):
    return "You requested: {}".format(path)

# For local development only
if __name__ == '__main__':
    app.run(debug=True)